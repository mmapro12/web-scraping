import requests


class CrimeReportUK:
    def __init__(self, location, date, crime_type="all-crime"):
        self.location = location
        self.crime_type = crime_type
        self.date = date
        self.crimes = self.findCrimes()
    
    def findCrimes(self):
        url = "https://data.police.uk/api/crimes-no-location"
        payload = {
            "category": self.crime_type,
            "force": self.location,
            "date": self.date
        }

        response = requests.get(url, params=payload)
        status = response.status_code
        if str(status) != "200":
            raise f"CrimeReportError: {status} status code is not acceptable."
        
        content = response.json()
        return content
    
    def getCrimesReport(self):
        json_file = self.crimes
        for item in json_file:
            try:
                print(f"""
                    Category: {item["category"]},
                    Outcome Status:

                      Category: {item["outcome_status"]["category"]}
                      Date: {item["outcome_status"]["date"]}

                    ID: {item["id"]}
                    Crime date: {item["month"]}
                """)

            except TypeError:
                print(f"""
                    Category: {item["category"]},
                    Outcome Status:

                      THERE AREN'T DATA ABOUT OUTCOME STATUS

                    ID: {item["id"]}
                    Crime date: {item["month"]}
                """)


app = CrimeReportUK("city-of-london", "2023-01,")
app.getCrimesReport()
    
