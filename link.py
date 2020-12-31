class Link:
    def compute(self, cluster, other, distances=None):
        pass


class SingleLink(Link):

    def compute(self, cluster, other, distances=None):
        """
        This method computes minimum distances between two different clusters.
        :param cluster: First object of Cluster
        :param other: Second object of Cluster
        :param distances: matrix of distances
        :return: Distance
        """
        minimum = distances[0][1]
        for sample1 in cluster.samples:
            for sample2 in other.samples:
                minimum = min(minimum, distances[sample1.s_id][sample2.s_id])
        return minimum


class CompleteLink(Link):

    def compute(self, cluster, other, distances=None):
        """
        This method computes maximum distances between two different clusters.
        :param cluster: First object of Cluster
        :param other: Second object of Cluster
        :param distances: matrix of distances
        :return: Distance
        """
        maximum = 0
        for sample1 in cluster.samples:
            for sample2 in other.samples:
                maximum = max(maximum, distances[sample1.s_id][sample2.s_id])
        return maximum
