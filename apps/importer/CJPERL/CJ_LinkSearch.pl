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
my $devKey = $ARGV[14]
my $websiteId = $ARGV[15];
my $soapclient = SOAP::Lite->service("https://linksearch.api.cj.com/wsdl/version2/linkSearchServiceV2.wsdl");
my $result = $soapclient->searchLinks($devKey, "", $websiteId, $advatiserId, $keywords, $category, $linkType, "", $language, $serviceableArea, $promotionType, "", "", $sortBy, $sortOrder, $startAt, $maxResults);
print $json->encode($result);
# eof
