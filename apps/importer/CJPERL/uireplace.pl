#!/usr/bin/perl -w

use strict;
use SOAP::Lite;
use JSON;
my $advatiserId = $ARGV[0];
my $json = new JSON;
my $devKey = "00b7aee2b960d09936d692f118ee179bfd785ae67677abb35ea773bdeccac02efc1f57cee3a220dce182b945beadec56549a1387d4ac6d422b0b0c3be1c49cd319/2394adf888e77f765ef451dda9694b5f3b2c288e7439ff61eb80011f585b07fe9c56f43d9d14a2df411c3df9d946c6c546fd032954ec9f90be91fa7afc4a22b1";
my $websiteId = 5377414;
my $soapclient = SOAP::Lite->service("https://product.api.cj.com/wsdl/version2/productSearchServiceV2.wsdl");
my $result = $soapclient->search($devKey, $websiteId, $advatiserId, "", "", "", "", "", "", "", "", "", "", "", "", "salePrice", "asc", 0, 100);
print $json->encode($result);
# eof
