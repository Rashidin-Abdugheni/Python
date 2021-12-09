
#To calculate the genome coverage, divide the number of bases sequenced by the estimated genome size,
# multiplied by % reads placed in contigs
#11 contigs
# 如： 1,514,603,088 / 2,100,000 x (96% of reads placed in contigs) = 692x
#is available from
#China General Microbiological Culture Collection Center, CGMCC 1.17902
#RawBases_
rawbases=1171132200
cleanBases=1118484740
genomesize=4356790
number_of_bases_sequenced =rawbases  #Raw bases
#Genomesize_
estimated_genome_size= genomesize #Total length
reads_placed_in_contigs= cleanBases/rawbases#Clean Bases / Raw Bases
print(reads_placed_in_contigs)
genome_coverage="{:.2f}".format((number_of_bases_sequenced/estimated_genome_size)*reads_placed_in_contigs)#print 2 decimal places

#format_float = "{:.2f}".format(genome_coverage)
#print(format_float)

print("%reads_placed_in_contigs=", "{:.2f}".format(reads_placed_in_contigs*100), "%") #print 2 decimal places
print("genome_coverage=", genome_coverage, "x")

#print(2679628734/2832851)