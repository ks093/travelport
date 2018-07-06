import urllib2
import base64
import suds

class HTTPSudsPreprocessor(urllib2.BaseHandler):

    def http_request(self, req):
        message = \
        """
<air:AvailabilitySearchReq xmlns:air="http://www.travelport.com/schema/air_v40_0" AuthorizedBy="user" TraceId="trace" TargetBranch="P151990">
  <com:BillingPointOfSaleInfo xmlns:com="http://www.travelport.com/schema/common_v40_0" OriginApplication="UAPI" />
  <air:SearchAirLeg>
    <air:SearchOrigin>
      <com:Airport xmlns:com="http://www.travelport.com/schema/common_v40_0" Code="IXC" />
    </air:SearchOrigin>
    <air:SearchDestination>
      <com:Airport xmlns:com="http://www.travelport.com/schema/common_v40_0" Code="BOM" />
    </air:SearchDestination>
    <air:SearchDepTime PreferredTime="2018-08-24" />
  </air:SearchAirLeg>
  <air:AirSearchModifiers>
    <air:PreferredProviders>
      <com:Provider xmlns:com="http://www.travelport.com/schema/common_v40_0" Code="1G" />
    </air:PreferredProviders>
  </air:AirSearchModifiers>
</air:AvailabilitySearchReq>
        """
        auth = base64.b64encode('Universal API/uAPI2765763013:Sx8r7tdsyzgRQQpT7D3mw4fSM')
        req.add_header('Content-Type', 'text/xml; charset=utf-8')
        req.add_header('Accept', 'gzip,deflate')
        req.add_header('Cache-Control','no-cache')
        req.add_header('Pragma', 'no-cache')
        req.add_header('SOAPAction', '')
        req.add_header('Authorization', 'Basic %s'%(auth))
        return req

    https_request = http_request


URL = "https://emea.universal-api.pp.travelport.com/B2BGateway/connect/uAPI"
https = suds.transport.https.HttpTransport()
opener = urllib2.build_opener(HTTPSudsPreprocessor)
https.urlopener = opener
suds.client.Client(URL, transport = https)