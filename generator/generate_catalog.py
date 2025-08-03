import os, json
from datetime import datetime

output_dir = "catalog"
os.makedirs(output_dir, exist_ok=True)

sample_data = {
    "metas": [
        {
            "id": "ott-movie-1",
            "name": "Sample Tamil OTT Movie",
            "type": "movie",
            "poster": "https://image.tmdb.org/t/p/w600_and_h900_bestv2/sample.jpg",
            "released": "2025-07-31"
        }
    ]
}

with open(f"{output_dir}/ott-movies.json", "w") as f:
    json.dump(sample_data, f, indent=2)

with open(f"{output_dir}/ott-shows.json", "w") as f:
    json.dump(sample_data, f, indent=2)

print("Catalog generated at", datetime.now())
