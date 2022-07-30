#!/usr/bin/env python3
################################################################################
# fetch_and_extract.py
#
# This program will fetch the publicly available binary from SCOM's website
# and extract the audio files in to the 2 sub-folders described in README.md.
#
# This program requires the following packages:
# 	wget
# 	sox
################################################################################

source_binary_url  = "http://www.scomcontrollers.com/downloads/SpLibEng_1.3.bin"
subdir_companded   = "c"
subdir_decompanded = "d"



print("begin...")
#===============================================================================
# first, fetch the binary
#===============================================================================
import os

if not os.path.exists("speech_library.bin"):
	os.system("wget " + source_binary_url + " -O speech_library.bin")

if not os.path.exists("speech_library.bin"):
	raise FileNotFoundError("Source binary isn't here.")



#===============================================================================
# now, let's have a look at that address table inside said binary...
#===============================================================================
def get_block_at(address_begin:int, address_end:int):
	with open("speech_library.bin", "rb") as source_file:
		source_file.seek(address_begin)
		return bytearray(source_file.read(address_end - address_begin))

def get_addr_at(address:int):
	return int.from_bytes(get_block_at(address, address + 3), "big")

# These values were correct with the binary at
# 	http://www.scomcontrollers.com/downloads/SpLibEng_1.3.bin
# Maybe they would change with another version, but I think it is unlikely.
seek_address_table = get_addr_at(0x100) # hex 00 02 00 =  dec     512 = This is were the address table begins.
seek_unknown       = get_addr_at(0x103) # hex 1A 06 5F =  dec 1705567 = I'm not sure what this address represents.
seek_EOF           = get_addr_at(0x106) # hex 76 20 6D =  dec 7741549 = This is where the binary says the EOF is.

seek_files         = [] # initialize a list for addresses to the audio samples

# The assumption here is that the first address referenced by the address
# table is a good indication of where the address table ends.
for address in range(seek_address_table, get_addr_at(seek_address_table), 4):
	seek_files.append( get_addr_at(address) )



#===============================================================================
# let's set up some methods for de-companding the audio...
# ... some of the complimentary methods are unnecessary for function of this
#     program, but are provided for completeness and future copy pasta.
#===============================================================================
from math import log

def sgn(x): return -1 if x < 0 else 1
def byte_to_float(b:int  ): return float((b-127.5)/127.5)
def float_to_byte(f:float): return int  ((f*127.5)+127.5)

def compand_byte(b:int):
	x = byte_to_float(b)
	return float_to_byte(
		sgn(x) * (
			log(  1 + 255*abs(x)  ) /
			log(  1 + 255         )
			)
		)

def decompand_byte(b:int):
	y = byte_to_float(b)
	return float_to_byte(
		sgn(y) * (
			(  (1+255)**abs(y) - 1  ) /
			255
			)
		)

# These two methods below use low-level access to the bytearray... so 'data'
# is actually being changed globally.  Also worth note is that companding and
# decompanding is lossy.  So, we should grab the pre-companded audio before
# we try decompanding the audio bytearray.

def compand_bytearray(data:bytearray):
	for index, byte in enumerate(data):
		data[index] = compand_byte(byte)
	return data

def decompand_bytearray(data:bytearray):
	for index, byte in enumerate(data):
		data[index] = decompand_byte(byte)
	return data



#===============================================================================
# Now, lets generate our output files...
#===============================================================================
def output_filename(subdir, num, extension):
	return subdir + "/" + str(num).rjust(4, '0') + "." + extension

def instantiate_dir(subdir):
	if not os.path.exists(subdir):
		os.mkdir(subdir)

instantiate_dir(subdir_companded  )
instantiate_dir(subdir_decompanded)

for index, begin in enumerate(seek_files):

	if begin == 0xFFFFFF:
		continue # the address 0xFFFFFF is a placeholder.  skip this one.

	end    = get_addr_at(begin) # the first 3 bytes are actually the end address.
	begin += 3                  # ... so the audio actually begins after 3 bytes.

	print("\tprocessing " +  str(index).rjust(4, '0') + " (beginning at " + hex(begin) + " and ending at " +hex(end) + ")")

	data = get_block_at(begin, end + 1) # include the data at the end address.
	data = bytearray(b'\x80' + data + b'\x80') # wrap that data with 1 sample of zero amplitude on each side

	# the bytearray is already companded, let's write that file first, then
	# decompand the bytearray and write that file.
	with open(output_filename(subdir_companded  , index, "raw"), "wb") as output: output.write(data)
	data = decompand_bytearray(data)
	with open(output_filename(subdir_decompanded, index, "raw"), "wb") as output: output.write(data)

	# use sox to make the raw audio files into wav files.
	os.system("sox -c 1 -b 8 -r 8000 -e unsigned-integer " + output_filename(subdir_companded  , index, "raw") + " "  + output_filename(subdir_companded  , index, "wav"))
	os.system("sox -c 1 -b 8 -r 8000 -e unsigned-integer " + output_filename(subdir_decompanded, index, "raw") + " "  + output_filename(subdir_decompanded, index, "wav"))

	# ... and remove the raw files.
	os.remove(output_filename(subdir_companded  , index, "raw"))
	os.remove(output_filename(subdir_decompanded, index, "raw"))



#===============================================================================
# ... and we're done.
#===============================================================================
print("...end.")
