#!/usr/bin/env perl

# cutting column by column
# Written by Ye Kyaw Thu, IDRI, CADT, Cambodia
# Preparation for 4th NLP/AI Workshop paper
# e.g. $ perl cut-column.pl <input-file> [1 or 2 or 3]

use strict;
use warnings;
use utf8;

binmode(STDIN, ":utf8");
binmode(STDOUT, ":utf8");
binmode(STDERR, ":utf8");

# the column number that you want to cut
my $column = $ARGV[1];
open (my $inputFILE,"<:encoding(utf8)", $ARGV[0]) or die "Couldn't open input file $ARGV[0]!, $!\n";

while (!eof($inputFILE)) {
     
    my $line = <$inputFILE>;
    if (($line ne '') & ($line !~ /^ *$/)) {
        chomp($line);
        $line =~ s/^\s+|\s+$//g;
        $line =~ s/ +/ /g;
       my ($col1, $col2, $col3) = split(/\|\|\|/, $line);
        if ($column eq "1") { 
           $col1 =~ s/^\s+|\s+$//g;
           print ("$col1\n");
        }elsif ($column eq "2"){
           $col2 =~ s/^\s+|\s+$//g;
           print ("$col2\n");
        }else {
           $col3 =~ s/^\s+|\s+$//g;
           print ("$col3\n");
        }
    }
}

close ($inputFILE);
