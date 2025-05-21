# URLs to download predictor data

ICEURLS = [
    {
        "name": "Beaufort_area_monthly",
        "skipentry": False,
        "URL": "https://www.ncei.noaa.gov/access/monitoring/regional-sea-ice/area/Beaufort/0/data.csv"
    },
    {
        "name": "Beaufort_extent_monthly",
        "skipentry": False,
        "URL": "https://www.ncei.noaa.gov/access/monitoring/regional-sea-ice/extent/Beaufort/0/data.csv"
    },
    {
        "name": "Chukchi_area_monthly",
        "skipentry": False,
        "URL": "https://www.ncei.noaa.gov/access/monitoring/regional-sea-ice/area/Chukchi/0/data.csv"
    },
    {
        "name": "Chukchi_extent_monthly",
        "skipentry": False,
        "URL": "https://www.ncei.noaa.gov/access/monitoring/regional-sea-ice/extent/Chukchi/0/data.csv"
    },
    {
        "name": "Bering_area_monthly",
        "skipentry": False,
        "URL": "https://www.ncei.noaa.gov/access/monitoring/regional-sea-ice/area/Bering/0/data.csv"
    },    
    {
        "name": "Bering_extent_monthly",
        "skipentry": False,
        "URL": "https://www.ncei.noaa.gov/access/monitoring/regional-sea-ice/extent/Bering/0/data.csv"
    },    
]

TELECONNECTIONURLS = [
    {
        "name": "Arctic_Oscillation",
        "shortname": "AO",
        "format": "PSL",
        "nodata": -999,
        "skipfooter": 3,
        "skipentry": False,
        "URL": "https://psl.noaa.gov/data/correlation/ao.data"
    },  
    {
        "name": "EastPac_NorthPac",
        "shortname": "EP-NP",
        "skipfooter": 3,
        "format": "PSL",
        "nodata": -99.90,
        "skipentry": False,
        "URL": "https://psl.noaa.gov/data/correlation/epo.data"
    },
    {
        "name": "Pacific_NA",
        "shortname": "PNA",
        "format": "PSL",
        "nodata": -99.90,
        "skipfooter": 3,
        "skipentry": False,
        "URL": "https://psl.noaa.gov/data/correlation/pna.data"
    },
    {
        "name": "Southern_Osc",
        "shortname": "SOI",
        "format": "PSL",
        "nodata": -99.99,
        "skipfooter": 3,
        "skipentry": False,
        "URL": "https://psl.noaa.gov/data/correlation/soi.data"
    },
    {
        "name": "Nino1_2",
        "shortname": "Nino1+2",
        "format": "PSL",
        "nodata": -99.99,
        "skipfooter": 3,
        "skipentry": False,
        "URL": "https://psl.noaa.gov/data/correlation/nina1.anom.data"
    },
    {
        "name": "Nino3",
        "shortname": "Nino3",
        "format": "PSL",
        "nodata": -99.99,
        "skipfooter": 3,
        "skipentry": False,
        "URL": "https://psl.noaa.gov/data/correlation/nina3.anom.data"
    },
    {
        "name": "Nino34",
        "shortname": "Nino3.4",
        "format": "PSL",
        "nodata": -99.99,
        "skipfooter": 3,
        "skipentry": False,
        "URL": "https://psl.noaa.gov/data/correlation/nina34.anom.data"
    },
    {
        "name": "Nino4",
        "shortname": "Nino4",
        "format": "PSL",
        "nodata": -99.99,
        "skipfooter": 3,
        "skipentry": False,
        "URL": "https://psl.noaa.gov/data/correlation/nina4.anom.data"
    },
    {
        "name": "Pacific_Decadal",
        "shortname": "PDO",
        "format": "special",
        "skipfooter": None,
        "nodata": 99.99,
        "skipentry": False,
        "URL": "https://www.ncei.noaa.gov/pub/data/cmb/ersst/v5/index/ersst.v5.pdo.dat"
    },
    {
        "name": "Oceanic_Nino",
        "shortname": "ONI",
        "format": "PSL",
        "skipfooter": 8,
        "nodata": -99.9,
        "skipentry": False,
        "URL": "https://psl.noaa.gov/data/correlation/oni.data"
    },
    {
        "name": "North_Pac_Pattern",
        "shortname": "NPI",
        "format": "YrMnth",
        "skipfooter": None,
        "skipentry": False,
        "URL": "https://climatedataguide.ucar.edu/sites/default/files/2024-04/npindex_monthly.txt"
        # "URL": "https://psl.noaa.gov/data/correlation/np.data"   # only to 2020
    },
    {
        "name": "cpc_multiple_teleconn",
        "shortname": None,
        "format": "Yr Mnth multiple",
        "skipheader": 17,
        "skipfooter": None,
        "nodata": -99.90,
        "skipentry": False,
        "URL": "https://ftp.cpc.ncep.noaa.gov/wd52dg/data/indices/tele_index.nh"
    },
    {
        "name": "Madden_Julian_Oscillation",
        "shortname": "MJO",
        "skipheader": 2,
        "format": "MJO",
        "nodata": -999,
        "skipfooter": None,
        "skipentry": True,
        "URL": "http://www.bom.gov.au/clim_data/IDCKGEM000/rmm.74toRealtime.txt"
    },  
]
