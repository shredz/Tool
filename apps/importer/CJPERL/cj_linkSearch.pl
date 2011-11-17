#!/usr/bin/perl -w
use strict;
use SOAP::Lite;
use JSON;
my $json = new JSON;
#"advertiserIds","keywords","category","linkType","linkSize","language","serviceableArea","promotionType","startDate","endDate","sortBy","sortOrder","startAt","maxResults"
my $advatiserId = $ARGV[0];
my $keywords = $ARGV[1];
my $category = $ARGV[2];
my $linkType = $ARGV[3];
my $linkSize = $ARGV[4];
my $language = $ARGV[5];
my $serviceableArea = $ARGV[6];
my $promotionType = $ARGV[7];
my $startDate = $ARGV[8];
my $endDate = $ARGV[9];
my $sortBy = $ARGV[10];
my $sortOrder = $ARGV[11];
my $startAt = $ARGV[12];
my $maxResults = $ARGV[13];
#print $maxResults;
my $devKey = "00b7aee2b960d09936d692f118ee179bfd785ae67677abb35ea773bdeccac02efc1f57cee3a220dce182b945beadec56549a1387d4ac6d422b0b0c3be1c49cd319/2394adf888e77f765ef451dda9694b5f3b2c288e7439ff61eb80011f585b07fe9c56f43d9d14a2df411c3df9d946c6c546fd032954ec9f90be91fa7afc4a22b1";
my $websiteId = 5377414;
my $soapclient = SOAP::Lite->service("https://linksearch.api.cj.com/wsdl/version2/linkSearchServiceV2.wsdl");
my $result = $soapclient->searchLinks($devKey, "", $websiteId, $advatiserId, $keywords, $category, $linkType, "", $language, $serviceableArea, $promotionType, "", "", $sortBy, $sortOrder, $startAt, $maxResults);
print $json->encode($result);
# eof
