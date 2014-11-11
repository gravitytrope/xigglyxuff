#!/usr/bin/perl
use strict;
use warnings;

print "Jello, Whirled!\n";
my ($c1, $c2, $c3);

my @xigList = qw(b d f g j l m n r s t w z br bl p dr fl fr gl gr pl pr sn sp st sw tr tw wr ch cl kl kr sch y);

print "\nHow many rows do you want?\n";
chomp(my $rows = <STDIN>);

if ($rows eq "\n" or $rows =~ /\D/) {
	print "Invalid input!";
	<>;
	exit;
} else {
	print "You chose: " . $rows . " rows.\n";
}

print "How many columns do you want? (must be an integer less than 7)\n";
chomp(my $columns = <STDIN>);

if ($columns eq "\n" or $columns =~ /\D/ or $columns > 6) {
	print "Invalid input!";
	<>;
	exit;
} else {
	print "You chose: " . $columns . " columns.\n";
}

my $total_numbers = $columns * $rows;

if ($total_numbers > 9999) {
	print "Too many numbers!";
	<>;
	exit;
}

my @num_array = ();
my ($box, $d, $f, $g, $h, $j);
my $line_segment = ("+-" . ("-" x 13) . "-");
my $a = 13 + 3;
my $line =  $line_segment x $columns;
my $linelength = length($line) * $columns;

if (length($linelength) > $columns) {
	print "Too many numbers!";
	<>;
	exit;
}

push(@num_array, " $line+\n");

print "\nHere are the usernames you requested.\n\n";

for (my $i = 1; $i <= $total_numbers; $i++) {
	$c1 = $xigList[rand @xigList];
	$c2 = $xigList[rand @xigList];
	while ($c2 eq $c1) {
		$c2 = $xigList[rand @xigList];
	}
	$j = ucfirst($c1) . "iggly" . $c2 . "uff";
	$g = ($a - length($j) - 1) / 2;
	$h = ($a - length($j)) / 2;
	$d = " " x $g;
	$f = " " x ($h - 1);
	$box = " |" . $d . $j . $f;
	
	if ($i%$columns == 0) {
			push(@num_array, $box . " |\n $line+\n");
		} else  {
			push(@num_array, $box);
		}
}

print @num_array;

<>;