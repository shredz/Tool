#!/usr/bin/perl -w

use strict;
use SOAP::Lite;
use Data::Dumper;
use JSON;
my $json = new JSON;
my $devKey = $ARGV[0]; #"00bbb2ce8435bc4a5d33e3d8c3191b9ebd5191a290c24ed00d843dcb4aafed8a6970509922b875302011d111ef8c3bfe5bade6d5f7399de82388530f7670bdef99/62c3eac14cd940341cdad6b38a61ab3ca9503dbf784f2a510275d5a3fe40bb246ada5171b6037ac44587b486bc5a86f714f5103e9a0557dc45130a1b9ed402b5";
my $date = $ARGV[1];
my $dateType = $ARGV[2];
my $advertiserIds = $ARGV[3];
my $websiteIds = $ARGV[4];
my $actionStatus = $ARGV[5];
my $actionTypes = $ARGV[6];
my $adIds = $ARGV[7];
my $countries = $ARGV[8];
my $correctionStatus = $ARGV[9];
my $sortBy = $ARGV[10];
my $sortOrder = $ARGV[11];
#print "Publisher Commission Search\n";
#"09/27/2011" , "posting"
my $soapclient = SOAP::Lite->service("https://pubcommission.api.cj.com/wsdl/version2/publisherCommissionServiceV2.wsdl");
my $result = $soapclient->findPublisherCommissions($devKey, $date, $dateType, $advertiserIds, $websiteIds, $actionStatus, $actionTypes, $adIds , $countries, $correctionStatus, $sortBy, $sortOrder);
#print Dumper($result);
print $json->encode($result);
# eof
