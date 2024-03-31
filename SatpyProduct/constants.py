from utils import generate24HourTimeRange,generateDayTimeRange ,generateNightTimeRange

day_and_night_products = [
    { "product_key": "dust" ,"product_title": 'Dust_RGB', "product_type": 'product' , "valid_time_args": generate24HourTimeRange()},
]

day_products = [
    { "product_key": "fog" ,"product_title": 'Fog', "product_type": 'product' , "valid_time_args": generateDayTimeRange()},
    { "product_key": "hrv_fog" ,"product_title": 'HRV_Fog', "product_type": 'product' , "valid_time_args": generateDayTimeRange()},
    { "product_key": "snow" ,"product_title": 'Snow_RGB', "product_type": 'product' , "valid_time_args": generateDayTimeRange()},
    { "product_key": "hrv_severe_storms" ,"product_title": 'HRV_Severe_Storms', "product_type": 'product' , "valid_time_args": generateDayTimeRange()},
    { "product_key": "day_microphysics" ,"product_title": 'Microphysics', "product_type": 'product' , "valid_time_args": generateDayTimeRange()},
]

night_products = [
    { "product_key": "night_fog" ,"product_title": 'Fog', "product_type": 'product' , "valid_time_args": generateNightTimeRange()},
    { "product_key": "night_microphysics" ,"product_title": 'Microphysics', "product_type": 'product' , "valid_time_args": generateNightTimeRange()},
]

band_products = [
    { "product_key": "HRV" ,"product_title": 'HRV', "product_type": 'band' , "valid_time_args": generate24HourTimeRange()},
    { "product_key": "IR_016" ,"product_title": 'IR_016', "product_type": 'band' , "valid_time_args": generate24HourTimeRange()},
    { "product_key": "IR_039" ,"product_title": 'IR_039', "product_type": 'band' , "valid_time_args": generate24HourTimeRange()},
    { "product_key": "IR_087" ,"product_title": 'IR_087', "product_type": 'band' , "valid_time_args": generate24HourTimeRange()},
    { "product_key": "IR_097" ,"product_title": 'IR_097', "product_type": 'band' , "valid_time_args": generate24HourTimeRange()},
    { "product_key": "IR_108" ,"product_title": 'IR_108', "product_type": 'band' , "valid_time_args": generate24HourTimeRange()},
    { "product_key": "IR_120" ,"product_title": 'IR_120', "product_type": 'band' , "valid_time_args": generate24HourTimeRange()},
    { "product_key": "IR_134" ,"product_title": 'IR_134', "product_type": 'band' , "valid_time_args": generate24HourTimeRange()},
    { "product_key": "VIS006" ,"product_title": 'VIS006', "product_type": 'band' , "valid_time_args": generate24HourTimeRange()},
    { "product_key": "VIS008" ,"product_title": 'VIS008', "product_type": 'band' , "valid_time_args": generate24HourTimeRange()},
    { "product_key": "WV_062" ,"product_title": 'WV_062', "product_type": 'band' , "valid_time_args": generate24HourTimeRange()},
    { "product_key": "WV_073" ,"product_title": 'WV_073', "product_type": 'band' , "valid_time_args": generate24HourTimeRange()},

]

products= band_products + day_and_night_products + night_products + day_products
    
export = products