"""
Traveling Salesman Problem solver.

Compares brute force and nearest neighbor algorithms.
"""

import argparse
import itertools
import json
import os
import time


def tsp_brute_force(distances, start=0):
    """Find the optimal route by checking every possible route."""
    n = len(distances)

    if n <= 1:
        return [start, start], 0

    best_route = None
    best_distance = float("inf")

    other_locations = [i for i in range(n) if i != start]

    for permutation in itertools.permutations(other_locations):
        route = [start] + list(permutation) + [start]

        total = sum(
            distances[route[i]][route[i + 1]]
            for i in range(len(route) - 1)
        )

        if total < best_distance:
            best_distance = total
            best_route = route

    return best_route, best_distance


def tsp_nearest_neighbor(distances, start=0):
    """Find a fast approximate route using nearest neighbor."""
    n = len(distances)

    if n <= 1:
        return [start, start], 0

    unvisited = set(range(n))
    unvisited.remove(start)

    route = [start]
    current = start
    total_distance = 0

    while unvisited:
        nearest = min(
            unvisited,
            key=lambda location: distances[current][location]
        )

        total_distance += distances[current][nearest]
        current = nearest
        route.append(current)
        unvisited.remove(current)

    total_distance += distances[current][start]
    route.append(start)

    return route, total_distance


def load_dataset(size):
    """Load a generated location dataset."""
    filename = f"locations/locations_{size}.json"

    with open(filename, "r", encoding="utf-8") as file:
        data = json.load(file)

    return data["distances"]


def test_small():
    """Check both algorithms on a small example."""
    distances = [
        [0, 10, 15, 20],
        [10, 0, 35, 25],
        [15, 35, 0, 30],
        [20, 25, 30, 0]
    ]

    route, distance = tsp_brute_force(distances)
    approximate_route, approximate_distance = tsp_nearest_neighbor(distances)

    assert abs(distance - 80) < 0.001
    assert approximate_distance >= distance

    print("Small tests passed!")
    print(f"Optimal route: {route}")
    print(f"Optimal distance: {distance}")
    print(f"Nearest neighbor route: {approximate_route}")
    print(f"Nearest neighbor distance: {approximate_distance}")


def time_brute_force():
    """Measure brute force runtime on increasing datasets."""
    for size in [5, 8, 10, 12, 15]:
        print(f"\nBrute force: {size} locations")

        try:
            distances = load_dataset(size)
        except FileNotFoundError:
            print("Dataset not found. Run location_generator.py first.")
            continue

        start_time = time.perf_counter()

        route, distance = tsp_brute_force(distances)

        elapsed = time.perf_counter() - start_time

        print(f"Runtime: {elapsed:.6f} seconds")
        print(f"Route distance: {distance:.2f}")
        print(f"Route: {route}")


def time_approximation():
    """Measure nearest neighbor runtime on every dataset."""
    for size in [5, 8, 10, 12, 15, 20]:
        print(f"\nNearest neighbor: {size} locations")

        distances = load_dataset(size)

        start_time = time.perf_counter()
        route, distance = tsp_nearest_neighbor(distances)
        elapsed = time.perf_counter() - start_time

        print(f"Runtime: {elapsed:.6f} seconds")
        print(f"Route distance: {distance:.2f}")


def compare_all():
    """Compare runtime and route quality on small datasets."""
    for size in [5, 8, 10]:
        distances = load_dataset(size)

        start_time = time.perf_counter()
        optimal_route, optimal_distance = tsp_brute_force(distances)
        brute_time = time.perf_counter() - start_time

        start_time = time.perf_counter()
        approx_route, approx_distance = tsp_nearest_neighbor(distances)
        approx_time = time.perf_counter() - start_time

        quality = (approx_distance / optimal_distance) * 100

        print(f"\nLocations: {size}")
        print(f"Brute force: {brute_time:.6f} seconds")
        print(f"Optimal distance: {optimal_distance:.2f}")
        print(f"Nearest neighbor: {approx_time:.6f} seconds")
        print(f"Approximate distance: {approx_distance:.2f}")
        print(f"Approximation quality: {quality:.2f}%")
        print(f"Optimal route: {optimal_route}")
        print(f"Approximate route: {approx_route}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--test-small", action="store_true")
    parser.add_argument("--time-brute-force", action="store_true")
    parser.add_argument("--time-approximation", action="store_true")
    parser.add_argument("--compare-all", action="store_true")

    args = parser.parse_args()

    if args.test_small:
        test_small()
    elif args.time_brute_force:
        time_brute_force()
    elif args.time_approximation:
        time_approximation()
    elif args.compare_all:
        compare_all()
    else:
        parser.print_help()