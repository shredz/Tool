#!/usr/bin/perl -w

use strict;
use SOAP::Lite;
use JSON;

my $advatiserId = $ARGV[2];
my $devKey = $ARGV[0];
my $websiteId = $ARGV[1];

my $soapclient = SOAP::Lite->service("https://product.api.cj.com/wsdl/version2/productSearchServiceV2.wsdl");
my $result = $soapclient->search($devKey, $websiteId, $advatiserId, "", "", "", "", "", "", "", "", "", "", "", "", "salePrice", "asc", 0, 100);
my $json = new JSON;
print $json->encode($result);
# eof
