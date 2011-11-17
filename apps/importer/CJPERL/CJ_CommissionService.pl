#!/usr/bin/perl -w

use strict;
use SOAP::Lite;
use Data::Dumper;
use JSON;

my $devKey = $ARGV[0];
my $websiteId = $ARGV[1];

my $soapclient = SOAP::Lite->service("https://rtpubcommission.api.cj.com/wsdl/version2/realtimeCommissionServiceV2.wsdl");
my $result = $soapclient->retrieveLatestTransactions($devKey, $websiteId, "3", "", "", "", "", "", "asc");
my $json = new JSON;
print $json->encode($result);
# eof
