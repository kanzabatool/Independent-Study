# -*- coding: utf-8 -*-
"""
Created on Fri Jun 29 14:38:00 2018

@author: KanzaBatool
"""

from Bio import pairwise2
from Bio.pairwise2 import format_alignment
from Bio.Seq import Seq

#bring dna sequence into our main code to keep things clean
dna = "GGTTCCGTGATGCACAGCTCCTTGGTTTTAATGAGTGTTTGTGAATGCAGTTGGTGAAGAACTCAGGCGAGCAGAGGCAATTGTGGACACCCCTACAGAAACGTCCTATACCCATGTGGCAATGCTCTGAAGAATAGCAGGGACCTCAGGAATGTCTATGGCCATACAATGACTAAACCAAATTCCCTCATCTTCTACTGTATCATTGTTTTAGGACTGACACTTATGAAAATCCAATTATCTGAGGAATGTGAGCTTATCATAAAGAGGCCAAACGCAAACCTTACCAGAGTGCCCAAGGACCTACCCTTGCAAACAACTACTTTAGATCTATCACAAAACAATATATCTGAGCTTCAGACTTCTGACATCCTCTCATTGTCCAAGCTGAGGGTCCTGATAATGTCCTACAACAGACTCCAGTATCTTAATATCAGTGTTTTCAAATTCAACACAGAGCTGGAATATTTGGATTTGTCCCACAATGAGCTAAAGGTGATCTTGTGCCACCCAACAGTCAGCCTCAAGCATTTGGACCTCTCCTTTAATGCCTTTGATGCCCTGCCTATATGCAAAGAATTTGGCAACATGTCCCAACTACAGTTCCTGGGGTTGAGCGGTTCTCGGGTACAAAGTTCAAGTGTGCAGCTGATTGCTCATTTGAACATCAGTAAGGTTTTGCTGGTGTTAGGAGATGCTTATGGGGAAAAAGAAGACCCCGAATCTCTTCGGCACGTTAGCACTGAGACTCTGCATATTGTTTTCCCGTCGAAAAGAGAATTCCGTTTTCTTCTGGATGTGTCCGTCAGCACTACGATCGGTTTGGAACTGTCTAACATCAAGTGTGTGCTTGAAGACCAGGGCTGCTCTTATTTCTTACGTGCTTTGTCAAAGCTTGGAAAGAATCTGAAGCTCTCAAATCTTACCCTGAACAATGTGGAAACAACGTGGAATTCCTTCATTAATATCCTCCAGATAGTTTGGCATACGCCAGTCAAATATTTCTCAATTTCAAATGTGAAGCTACAAGGTCAACTTGCCTTCAGGATGTTCAATTATTCTGACACTTCTCTGAAGGCTTTGTCGATACATCAAGTTGTCACTGATGTCTTCAGCTTCCCCCAAAGTTACATATACAGTATCTTTGCCAATATGAACATCCAAAACTTTACAATGTCTGGAACACACATGGTCCACATGCTGTGCCCGTCCCAAGTTAGCCCATTTCTGCATGTGGACTTTACAGATAACCTTTTAACAGACATGGTTTTTAAAGACTGTAGAAACTTAGTTAGATTGAAAACACTTAGTTTACAAAAGAATCAGTTAAAAAACCTTGAGAATATAATCCTCACATCTGCAAAGATGACATCCCTACAAAAACTAGACATTAGCCAGAATTCTCTAAGGTACAGCGATGGGGGAATCCCATGCGCCTGGACCCAGAGTTTGTTAGTTTTAAATTTGTCTTCGAATATGCTTACAGGCTCTGTCTTCAGATGCTTACCTCCCAAAGTCAAGGTCCTTGACCTTCACAACAACAGGATAATGAGCATCCCTAAAGATGTCACCCACCTGCAGGCTTTGCAGGAACTCAATGTAGCATCCAACTCCTTAACTGACCTTCCTGGGTGCGGGGCCTTCAGCAGCCTTTCTGTGCTGGTCATCGACCATAACTCAGTTTCCCATCCCTCTGAGGATTTCTTCCAGAGCTGTCAGAATATTAGATCCCTAACAGCGGGAAACAACCCATTCCAATGCACATGTGAGCTGAGGGACTTTGTCAAGAACATAGGCTGGGTAGCAAGAGAAGTGGTGGAGGGCTGGCCTGACTCTTACAGGTGTGACTACCCAGAAAGCTCTAGGGGAACTGCACTGAGGGACTTCCACATGTCTCCACTATCCTGTGATACTGTTCTGCTGACTGTCACCATCGGGGCCACTATGCTGGTGCTGGCTGTCACTGGGGCTTTCCTCTGTCTCTACTTTGACCTGCCCTGGTATGTGAGGATGCTGTGTCAGTGGACACAGACCAGGCACAGGGCCAGGCACATCCCCTTAGAGGAACTCCAGAGAAACCTCCAGTTCCATGCTTTTGTCTCATACAGTGGGCATGATTCTGCCTGGGTGAAGAACGAATTACTACCCAACCTAGAGAAAGATGACATCCAGATTTGCCTCCATGAGAGGAACTTTGTCCCTGGCAAGAGCATTGTGGAGAACATCATCAATTTCATTGAGAAGAGTTACAAGTCCATCTTTGTGCTGTCTCCCCACTTCATCCAGAGTGAGTGGTGTCATTATGAACTCTATTTTGCCCATCACAATCTCTTCCATGAAGGCTCTGATAACTTAATCCTCATCTTGCTGGCACCCATTCCCCAGTACTCCATCCCTACCAATTACCACAAGCTCAAAACTCTCATGTCACGAAGGACCTATCTGGAATGGCCCACAGAGAAGAACAAGCATGGACTTTTTTGGGCAAACCTAAGAGCATCCATTAATGTTAAGCTGGTTAACCAGGCAGAAGGAACGTGTTACACACAGCAATAAGAATATCCACC"

def loop():

	coding_dna = Seq(dna)
	orf1 = coding_dna.translate()
	print ("**********************ORF1***********************")
	print (orf1)
	print ("\n\n")

	coding_dna = Seq(dna[1:])
	orf2 = coding_dna.translate()
	print ("**********************ORF2***********************")
	print (orf2)
	print ("\n\n")

	coding_dna = Seq(dna[2:])
	orf3 = coding_dna.translate()
	print ("**********************ORF3***********************")
	print (orf3)
	print ("\n\n")

	coding_dna = Seq(dna)
	coding_dna_reverse_comp = coding_dna.reverse_complement()
	orf4 = coding_dna_reverse_comp.translate()
	print ("**********************ORF4***********************")
	print (orf4)
	print ("\n\n")

	coding_dna = Seq(dna[:-1])
	coding_dna_reverse_comp = coding_dna.reverse_complement()
	orf5 = coding_dna_reverse_comp.translate()
	print ("**********************ORF5***********************")
	print (orf5)
	print ("\n\n")

	coding_dna = Seq(dna[:-2])
	coding_dna_reverse_comp = coding_dna.reverse_complement()
	orf6 = coding_dna_reverse_comp.translate()
	print ("**********************ORF6***********************")
	print (orf6)
	print ("\n\n")

def match():
	String1 = 'ACCGTTTTTTACACAC'
	String2 = 'ACGACACGTAC'
	alignments = pairwise2.align.globalxx(String1, String2)
	print(format_alignment(*alignments[0]))

def main():
	loop()
	match()

main()
