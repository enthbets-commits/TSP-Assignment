"""
Generates emergency location datasets for the Traveling Salesman Problem.
"""

import json
import os
import random
import math


def generate_locations():
    """Generate datasets containing emergency locations."""

    if not os.path.exists("locations"):
        os.makedirs("locations")

    sizes = [5, 8, 10, 12, 15, 20]

    print("Generating emergency location datasets...\n")

    for size in sizes:
        locations = []

        for i in range(size):
            locations.append({
                "id": i,
                "name": f"Location {i + 1}",
                "x": round(random.uniform(0, 100), 2),
                "y": round(random.uniform(0, 100), 2)
            })

        distances = []

        for i in range(size):
            row = []

            for j in range(size):
                distance = math.sqrt(
                    (locations[i]["x"] - locations[j]["x"]) ** 2
                    + (locations[i]["y"] - locations[j]["y"]) ** 2
                )

                row.append(round(distance, 2))

            distances.append(row)

        data = {
            "size": size,
            "locations": locations,
            "distances": distances
        }

        filename = f"locations/locations_{size}.json"

        with open(filename, "w", encoding="utf-8") as file:
            json.dump(data, file, indent=2)

        print(f"Generated {filename}")

    print("\nLocation generation complete!")


if __name__ == "__main__":
    generate_locations()