#!/usr/bin/env python

"""
A kmeans clustering tool that uses multiprocessing to speed up the process.
The Python click command-line tool library allows us to create queries that parameterize the clustering process.
"""
import click
from multiprocessing import Pool, cpu_count
from sklearn.datasets import make_blobs
from sklearn.cluster import KMeans
import time

#pylint: disable=W0632
def do_kmeans(n_samples):
    """KMeans clustering on generated data"""

    X,_ = make_blobs(n_samples, centers=3, n_features=10,
                random_state=0) 
    kmeans = KMeans(n_clusters=3)
    t0 = time.time()
    kmeans.fit(X)
    print(f"KMeans cluster fit in {time.time()-t0}")

def run_parallel(count,processes):
    """Run Everything"""

    count = int(count)
    processes = int(processes)
    t0 = time.time()
    with Pool(processes) as p:
        p.map(do_kmeans, [100000 for x in range(count)])
    print(f"Performed {count} KMeans in total time: {time.time()-t0} using processes total: {processes}")

@click.group()
def cli():
    """A kmeans clustering tool that uses multiprocessing to speed up the process."""

@cli.command("cpucount")
def cpucount():
    """Prints the number of CPUs on the system."""

    # Print the number of CPUs on the system using click colors
    click.secho(f"Number of CPUs: {cpu_count()}", fg="green")

@cli.command("cluster")
@click.option("--count", default=cpu_count(), help="Number of KMeans to run.")
@click.option("--processes", default=cpu_count(), help="Number of processes to use.")
def cluster(count, processes):
    """Run KMeans clustering on generated data.
    
    Example: python mp_tool.py cluster --count 10 --processes 5
    """

    run_parallel(count, processes)


if __name__ == "__main__":
    cli()
