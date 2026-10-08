# -*- coding: utf-8 -*-
"""Extra per-area content: hero images, numbered driving directions, parking notes.
Keyed by area slug. Merged into AREAS entries in build.py."""

AREA_EXTRAS = {
    "north-york": {
        "img": "north-york.jpg",
        "img_alt": "Dufferin Street in North York near Apex Collision Center",
        "directions": [
            "Head to Dufferin Street between Finch Avenue and Sheppard Avenue in North York.",
            "Look for 4544 Dufferin Street, Units 41 and 42, on the east side of Dufferin.",
            "Pull into our lot. Parking is free and right at the door.",
            "Come inside or call (416) 661-6665 and we will get your car checked in.",
        ],
        "parking": "Free parking at the shop. Walk ins welcome for inspections, diagnostics, oil changes and battery checks.",
    },
    "toronto": {
        "img": "toronto.jpg",
        "img_alt": "Midtown Toronto street near Yorkdale, on the way to Apex Collision Center",
        "directions": [
            "From Yorkdale or the Allen Expressway, take Allen Road north to Highway 401.",
            "Take Highway 401 west to the Dufferin Street exit.",
            "Head north on Dufferin Street to 4544 Dufferin Street, Units 41 and 42.",
            "Free parking is at the shop. Call (416) 661-6665 if you need help finding us.",
        ],
        "parking": "Free parking at the shop, right off the 401 at Dufferin.",
    },
    "downtown-toronto": {
        "img": "downtown-toronto.jpg",
        "img_alt": "Downtown Toronto skyline, where many Apex Collision Center customers drive from",
        "directions": [
            "From the downtown core, take Allen Road north to Highway 401.",
            "Take Highway 401 west to the Dufferin Street exit.",
            "Head north on Dufferin Street to 4544 Dufferin Street, Units 41 and 42.",
            "Park free at the shop. Saturday appointments, 10:00 AM to 3:00 PM, suit drivers who cannot spare a weekday.",
        ],
        "parking": "Free parking at the shop. Saturday hours make the drive easy.",
    },
    "scarborough": {
        "img": "scarborough.jpg",
        "img_alt": "Scarborough street view, an easy drive from Apex Collision Center via Highway 401",
        "directions": [
            "Take Highway 401 westbound across the city.",
            "Exit at Dufferin Street and head north.",
            "Continue to 4544 Dufferin Street, Units 41 and 42, in North York.",
            "Book ahead for bigger repairs so parts and a lift are ready when you arrive.",
        ],
        "parking": "Free parking at the shop, minutes off the 401.",
    },
    "mississauga": {
        "img": "mississauga.jpg",
        "img_alt": "Mississauga city centre, about 20 to 30 minutes from Apex Collision Center",
        "directions": [
            "Take Highway 401 east to the Dufferin Street exit, or Highway 427 north to the 401.",
            "Head north on Dufferin Street to 4544 Dufferin Street, Units 41 and 42.",
            "Allow 20 to 30 minutes depending on where in Mississauga you start and traffic.",
            "Saturday appointments work well for the drive. Call (416) 661-6665 to book.",
        ],
        "parking": "Free parking at the shop. All 22 services available to Mississauga drivers.",
    },
    "etobicoke": {
        "img": "etobicoke.jpg",
        "img_alt": "Etobicoke streetscape, minutes from Apex Collision Center in North York",
        "directions": [
            "Take Highway 401 east to the Dufferin Street exit.",
            "Head north on Dufferin Street to 4544 Dufferin Street, Units 41 and 42.",
            "The trip is about 15 to 20 minutes from most of Etobicoke.",
            "Same day service is often available for maintenance and diagnostics. Call ahead to confirm.",
        ],
        "parking": "Free parking at the shop, close enough for a lunch break oil change.",
    },
    "vaughan": {
        "img": "vaughan.jpg",
        "img_alt": "Vaughan streetscape, a straight drive south to Apex Collision Center",
        "directions": [
            "Take Dufferin Street straight south from Vaughan.",
            "Continue to 4544 Dufferin Street, Units 41 and 42, in North York.",
            "The drive is typically 15 to 20 minutes. Highway 400 south to Finch or the 401 also works.",
            "Call (416) 661-6665 with your symptoms for an honest estimate range before you drive down.",
        ],
        "parking": "Free parking at the shop, right on Dufferin.",
    },
    "markham": {
        "img": "markham.jpg",
        "img_alt": "Markham main street, one highway away from Apex Collision Center",
        "directions": [
            "Take Highway 404 south to Highway 401 west.",
            "Exit at Dufferin Street and head north.",
            "Continue to 4544 Dufferin Street, Units 41 and 42, in North York.",
            "Allow 20 to 30 minutes. Bring the other shop quote if you want a second opinion.",
        ],
        "parking": "Free parking at the shop, minutes off the 401.",
    },
}
