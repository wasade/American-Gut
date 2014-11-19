from numpy import nan

# Adapted from the information in
#   Wikipedia. "List of US state abbreviations." Updated 14 May 2014.
#       acessed 7 June 2014.
#       http://en.wikipedia.org/wiki/List_of_U.S._state_abbreviations

us_state_map = {nan: nan,
                'AL': 'AL', 'Alabama': 'AL', 'ALABAMA': 'AL',
                'AK': 'AK', 'Alaska': 'AK', 'ALASKA': 'AK',
                'AZ': 'AZ', 'Arizona': 'AZ', 'ARIZONA': 'AZ',
                'AR': 'AR', 'Arkansas': 'AR', 'ARKANSAS': 'AR',
                'CA': 'CA', 'California': 'CA', 'CALIFORNIA': 'CA',
                'CO': 'CO', 'Colorado': 'CO', 'COLORADO': 'CO',
                'CT': 'CT', 'Connecticut': 'CT', 'CONNECTICUT': 'CT',
                'DE': 'DE', 'Delaware': 'DE', 'DELAWARE': 'DE',
                'DC': 'DC', 'District of Columbia': 'DC',
                'DISTRICT OF COLUMBIA': 'DC',
                'FL': 'FL', 'Florida': 'FL', 'FLORIDA': 'FL',
                'GA': 'GA', 'Georgia': 'GA', 'GEORGIA': 'GA',
                'HI': 'HI', 'Hawaii': 'HI', 'HAWAII': 'HI',
                'ID': 'ID', 'Idaho': 'ID', 'IDAHO': 'ID',
                'IL': 'IL', 'Illinois': 'IL', 'ILLINOIS': 'IL',
                'IN': 'IN', 'Indiana': 'IN', 'INDIANA': 'IN',
                'IA': 'IA', 'Iowa': 'IA', 'IOWA': 'IA',
                'KS': 'KS', 'Kansas': 'KS', 'KANSAS': 'KS',
                'KY': 'KY', 'Kentucky': 'KY', 'KENTUCKY': 'KY',
                'LA': 'LA', 'Louisiana': 'LA', 'LOUISIANA': 'LA',
                'MS': 'MS', 'MISSISSIPPI': 'MS', 'MISSISSIPPI': 'MS',
                'ME': 'ME', 'Maine': 'ME', 'MAINE': 'ME',
                'MD': 'MD', 'Maryland': 'MD', 'MARYLAND': 'MD',
                'MA': 'MA', 'Massachusetts': 'MA', 'MASSACHUSETTS': 'MA',
                'MI': 'MI', 'Michigan': 'MI', 'MICHIGAN': 'MI',
                'MN': 'MN', 'Minnesota': 'MN', 'MINNESOTA': 'MN',
                'MS': 'MS', 'Mississippi': 'MS', 'MISSISSIPPI': 'MS',
                'MO': 'MO', 'Missouri': 'MO', 'MISSOURI': 'MO',
                'MT': 'MT', 'Montana': 'MT', 'MONTANA': 'MT',
                'NE': 'NE', 'Nebraska': 'NE', 'NEBRASKA': 'NE',
                'NV': 'NV', 'Nevada': 'NV', 'NEVADA': 'NV',
                'NH': 'NH', 'New Hampshire': 'NH', 'NEW HAMPSHIRE': 'NH',
                'NJ': 'NJ', 'New Jersey': 'NJ', 'NEW JERSEY': 'NJ',
                'NM': 'NM', 'New Mexico': 'NM', 'NEW MEXICO': 'NM',
                'NY': 'NY', 'New York': 'NY', 'NEW YORK': 'NY',
                'NC': 'NC', 'North Carolina': 'NC', 'NORTH CAROLINA': 'NC',
                'ND': 'ND', 'North Dakota': 'ND', 'NORTH DAKOTA': 'ND',
                'OH': 'OH', 'Ohio': 'OH', 'OHIO': 'OH',
                'OK': 'OK', 'Oklahoma': 'OK', 'OKLAHOMA': 'OK',
                'OR': 'OR', 'Oregon': 'OR', 'OREGON': 'OR',
                'PA': 'PA', 'Pennsylvania': 'PA', 'PENNSYLVANIA': 'PA',
                'PR': 'PR', 'Puerto Rico': 'PR', 'PUERTO RICO': 'PR',
                'RI': 'RI', 'Rhode Island': 'RI', 'RHODE ISLAND': 'RI',
                'SC': 'SC', 'South Carolina': 'SC', 'SOUTH CAROLINA': 'SC',
                'SD': 'SD', 'South Dakota': 'SD', 'SOUTH DAKOTA': 'SD',
                'TN': 'TN', 'Tennessee': 'TN', 'TENNESSEE': 'TN',
                'TX': 'TX', 'Texas': 'TX', 'TEXAS': 'TX',
                'UT': 'UT', 'Utah': 'UT', 'UTAH': 'UT',
                'VT': 'VT', 'Vermont': 'VT', 'VERMONT': 'VT',
                'VI': 'VI', 'Virgin Islands': 'VI', 'VIRGIN ISLANDS': 'VI',
                'VA': 'VA', 'Virginia': 'VA', 'VIRGINIA': 'VA',
                'WA': 'WA', 'Washington': 'WA', 'WASHINGTON': 'WA',
                'WV': 'WV', 'West Virginia': 'WV', 'WEST VIRGINIA': 'WV',
                'WI': 'WI', 'Wisconsin': 'WI', 'WISCONSIN': 'WI',
                'WY': 'WY', 'Wyoming': 'WY', 'WYOMING': 'WY'}


# These dictionaries are adapted from information presented in
#   Wikipedia. "Canadian postal abbrevations for providence and territories."
#        updated 30 May 2014. acessed 7 June 2014.
#        http://en.wikipedia.org/wiki/
#               Canadian_postal_abbreviations_for_provinces_and_territories

canadian_map_english = {nan: nan,
                        'AB': 'AB', 'Alberta': 'AB', 'ALBERTA': 'AB',
                        'BC': 'BC', 'British Columbia': 'BC',
                        'BRITISH COLUMBIA': 'BC',
                        'MB': 'MB', 'Manitoba': 'MB', 'MANITOBA': 'MB',
                        'NB': 'NB', 'New Brunswick': 'NB',
                        'NEW BRUNSWICK': 'NB',
                        'NL': 'NL', 'Newfoundland and Laborador': 'NL',
                        'Newfoundland': 'NL', 'Laborador': 'NL',
                        'NEWFOUNDLAND AND LABORADOR': 'NL', 'NEWFOUNDLAND':
                        'NL', 'LABORADOR': 'NL',
                        'NS': 'NS', 'Nova Scotia': 'NS', 'NOVA SCOTIA': 'NS',
                        'NT': 'NT', 'Northwest Territories': 'NT',
                        'NORTHWEST TERRITORIES': 'NT',
                        'NU': 'NU', 'Nunavut': 'NU', 'NUNAVUT': 'NU',
                        'ON': 'ON', 'Ontario': 'ON', 'ONTARIO': 'ON',
                        'PE': 'PE', 'Prince Edward Island': 'PE',
                        'PRINCE EDWARD ISLAND': 'PE',
                        'QC': 'QC', 'Quebec': 'QC', 'QUEBEC': 'QC',
                        'SK': 'SK', 'Saskatchewan': 'SK', 'SASKATCHEWAN': 'SK',
                        'YT': 'YT', 'Yukon': 'YT', 'YUKON': 'YT'}

# The next two dictionaries are adapted from information presented in
#       Wikipedia. "List of regions of the United States". updated 7 June 2014,
#           accessed 7 June 2014.
#           http://en.wikipedia.org/wiki/List_of_regions_of_the_United_States

regions_by_state = {nan: {'Census_1': nan,
                          'Census_2': nan,
                          'Economic': nan},
                    'AK': {'Census_1': 'West',
                           'Census_2': 'Pacific',
                           'Economic': 'Far West'},
                    'AL': {'Census_1': 'South',
                           'Census_2': 'East South Central',
                           'Economic': 'Southeast'},
                    'AR': {'Census_1': 'South',
                           'Census_2': 'West South Central',
                           'Economic': 'Southeast'},
                    'AZ': {'Census_1': 'West',
                           'Census_2': 'Mountain',
                           'Economic': 'Southwest'},
                    'CA': {'Census_1': 'West',
                           'Census_2': 'Pacific',
                           'Economic': 'Far West'},
                    'CO': {'Census_1': 'West',
                           'Census_2': 'Mountain',
                           'Economic': 'Rocky Mountain'},
                    'CT': {'Census_1': 'Northeast',
                           'Census_2': 'New England',
                           'Economic': 'New England'},
                    'DC': {'Census_1': 'South',
                           'Census_2': 'South Atlantic',
                           'Economic': 'Mideast'},
                    'DE': {'Census_1': 'Northeast',
                           'Census_2': 'Mid-Atlantic',
                           'Economic': 'Mideast'},
                    'FL': {'Census_1': 'South',
                           'Census_2': 'South Atlantic',
                           'Economic': 'Southeast'},
                    'GA': {'Census_1': 'South',
                           'Census_2': 'South Atlantic',
                           'Economic': 'Southeast'},
                    'HI': {'Census_1': 'West',
                           'Census_2': 'Pacific',
                           'Economic': 'Far West'},
                    'IA': {'Census_1': 'Midwest',
                           'Census_2': 'West North Central',
                           'Economic': 'Plains'},
                    'ID': {'Census_1': 'West',
                           'Census_2': 'Mountain',
                           'Economic': 'Rocky Mountain'},
                    'IL': {'Census_1': 'Midwest',
                           'Census_2': 'East North Central',
                           'Economic': 'Great Lakes'},
                    'IN': {'Census_1': 'Midwest',
                           'Census_2': 'East North Central',
                           'Economic': 'Great Lakes'},
                    'KS': {'Census_1': 'Midwest',
                           'Census_2': 'West North Central',
                           'Economic': 'Plains'},
                    'KY': {'Census_1': 'South',
                           'Census_2': 'East South Central',
                           'Economic': 'Southeast'},
                    'LA': {'Census_1': 'South',
                           'Census_2': 'West South Central',
                           'Economic': 'Southeast'},
                    'MA': {'Census_1': 'Northeast',
                           'Census_2': 'New England',
                           'Economic': 'New England'},
                    'MD': {'Census_1': 'South',
                           'Census_2': 'South Atlantic',
                           'Economic': 'Mideast'},
                    'ME': {'Census_1': 'Northeast',
                           'Census_2': 'New England',
                           'Economic': 'New England'},
                    'MI': {'Census_1': 'Midwest',
                           'Census_2': 'East North Central',
                           'Economic': 'Great Lakes'},
                    'MN': {'Census_1': 'Midwest',
                           'Census_2': 'West North Central',
                           'Economic': 'Plains'},
                    'MO': {'Census_1': 'Midwest',
                           'Census_2': 'West North Central',
                           'Economic': 'Plains'},
                    'MS': {'Census_1': 'South',
                           'Census_2': 'East South Central',
                           'Economic': 'Southeast'},
                    'MT': {'Census_1': 'West',
                           'Census_2': 'Mountain',
                           'Economic': 'Rocky Mountain'},
                    'NC': {'Census_1': 'South',
                           'Census_2': 'South Atlantic',
                           'Economic': 'Southeast'},
                    'ND': {'Census_1': 'Midwest',
                           'Census_2': 'West North Central',
                           'Economic': 'Plains'},
                    'NE': {'Census_1': 'Midwest',
                           'Census_2': 'West North Central',
                           'Economic': 'Plains'},
                    'NH': {'Census_1': 'Northeast',
                           'Census_2': 'New England',
                           'Economic': 'New England'},
                    'NJ': {'Census_1': 'Northeast',
                           'Census_2': 'Mid-Atlantic',
                           'Economic': 'Mideast'},
                    'NM': {'Census_1': 'West',
                           'Census_2': 'Mountain',
                           'Economic': 'Southwest'},
                    'NV': {'Census_1': 'West',
                           'Census_2': 'Mountain',
                           'Economic': 'Far West'},
                    'NY': {'Census_1': 'Northeast',
                           'Census_2': 'Mid-Atlantic',
                           'Economic': 'Mideast'},
                    'OH': {'Census_1': 'Midwest',
                           'Census_2': 'East North Central',
                           'Economic': 'Great Lakes'},
                    'OK': {'Census_1': 'South',
                           'Census_2': 'West South Central',
                           'Economic': 'Southwest'},
                    'OR': {'Census_1': 'West',
                           'Census_2': 'Pacific',
                           'Economic': 'Far West'},
                    'PA': {'Census_1': 'Northeast',
                           'Census_2': 'Mid-Atlantic',
                           'Economic': 'Mideast'},
                    'PR': {'Census_1': 'Territories',
                           'Census_2': 'Territories',
                           'Economic': 'Territories'},
                    'RI': {'Census_1': 'Northeast',
                           'Census_2': 'New England',
                           'Economic': 'New England'},
                    'SC': {'Census_1': 'South',
                           'Census_2': 'South Atlantic',
                           'Economic': 'Southeast'},
                    'SD': {'Census_1': 'Midwest',
                           'Census_2': 'West North Central',
                           'Economic': 'Plains'},
                    'TN': {'Census_1': 'South',
                           'Census_2': 'East South Central',
                           'Economic': 'Southeast'},
                    'TX': {'Census_1': 'South',
                           'Census_2': 'West South Central',
                           'Economic': 'Southwest'},
                    'UT': {'Census_1': 'West',
                           'Census_2': 'Mountain',
                           'Economic': 'Rocky Mountain'},
                    'VA': {'Census_1': 'South',
                           'Census_2': 'South Atlantic',
                           'Economic': 'Southeast'},
                    'VI': {'Census_1': 'Territories',
                           'Census_2': 'Territories',
                           'Economic': 'Territories'},
                    'VT': {'Census_1': 'Northeast',
                           'Census_2': 'New England',
                           'Economic': 'New England'},
                    'WA': {'Census_1': 'West',
                           'Census_2': 'Pacific',
                           'Economic': 'Far West'},
                    'WI': {'Census_1': 'Midwest',
                           'Census_2': 'East North Central',
                           'Economic': 'Great Lakes'},
                    'WV': {'Census_1': 'South',
                           'Census_2': 'South Atlantic',
                           'Economic': 'Southeast'},
                    'WY': {'Census_1': 'West',
                           'Census_2': 'Mountain',
                           'Economic': 'Rocky Mountain'}}

regions = {'Census_1': {'Northeast': {'CT', 'ME', 'MA', 'NH', 'RI', 'VT', 'NJ',
                                      'DE', 'NY', 'PA'},
                        'Midwest': {'IL', 'IN', 'MI', 'OH', 'WI', 'IA', 'KS',
                                    'MN', 'MO', 'NE', 'ND', 'SD'},
                        'South': {'FL', 'GA', 'MD', 'NC', 'SC', 'DC', 'VA',
                                  'WV', 'AL', 'KY', 'MS', 'TN', 'AR', 'LA',
                                  'OK', 'TX'},
                        'West': {'AZ', 'CO', 'ID', 'MT', 'NV', 'NM', 'UT',
                                 'WY', 'AK', 'CA', 'HI', 'OR', 'WA'},
                        'Territories': {'PR', 'VI', 'AS', 'GU', 'MP'}},
           'Census_2': {'New England': {'CT', 'ME', 'MA', 'NH', 'RI', 'VT'},
                        'Mid-Atlantic': {'NJ', 'DE', 'NY', 'PA'},
                        'East North Central': {'IL', 'IN', 'MI', 'OH', 'WI'},
                        'West North Central': {'IA', 'KS', 'MN', 'MO', 'NE',
                                               'ND', 'SD'},
                        'South Atlantic': {'FL', 'GA', 'MD', 'NC', 'SC', 'DC',
                                           'VA', 'WV'},
                        'East South Central': {'AL', 'KY', 'MS', 'TN'},
                        'West South Central': {'AR', 'LA', 'OK', 'TX'},
                        'Mountain': {'AZ', 'CO', 'ID', 'MT', 'NV', 'NM', 'UT',
                                     'WY'},
                        'Pacific': {'AK', 'CA', 'HI', 'OR', 'WA'},
                        'Territories': {'PR', 'VI', 'GU'}},
           'Economic': {'New England': {'CT', 'ME', 'MA', 'NH', 'RI', 'VT'},
                        'Mideast': {'NJ', 'DE', 'NY', 'PA', 'DC', 'MD'},
                        'Great Lakes': {'IL', 'IN', 'OH', 'MI', 'WI'},
                        'Plains': {'IA', 'KS', 'MN', 'MO', 'NE', 'ND', 'SD'},
                        'Southeast': {'AL', 'AR', 'FL', 'GA', 'KY', 'LA', 'MS',
                                      'NC', 'SC', 'TN', 'VA', 'WV'},
                        'Southwest': {'AZ', 'NM', 'OK', 'TX'},
                        'Rocky Mountain': {'CO', 'ID', 'MT', 'UT', 'WY'},
                        'Far West': {'AK', 'CA', 'HI', 'NV', 'OR', 'WA'},
                        'Territories': {'PR', 'VI', 'AS', 'GU', 'MP'}}}