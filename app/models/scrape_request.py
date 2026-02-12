from pydantic import BaseModel,HttpUrl,field_validator
from urllib.parse import urlparse
import ipaddress

class ScraperRequest(BaseModel):
    url : HttpUrl

    @field_validator("url") 
    @classmethod
    def validate_url(cls,v):# Validate that the URL is not private or local
        parsed = urlparse(str(v)) # Convert HttpUrl to string for parsing    

        #Blocked localhost
        if parsed.hostname in ("localhost","127.0.0.1"):
            raise ValueError("Localhost URLs are not allowed")
        
        #Blocked private IPs
        try:
            ip = ipaddress.ip_address(parsed.hostname)
            if ip.is_private:
                raise ValueError("Private IP addresses are not allowed")
        except ValueError:
            #hostname is not an IP-> FINE
            pass
        return v
