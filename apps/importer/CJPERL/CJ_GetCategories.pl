#!/usr/bin/perl -w

use strict;
use SOAP::Lite;
use JSON;
my $json = new JSON;

my $devKey = $ARGV[0];
my $soapclient = SOAP::Lite->service("https://linksearch.api.cj.com/wsdl/version2/supportServiceV2.wsdl");
my $result = $soapclient->getCategories($devKey, "en");
print $json->encode($result);
# eof
