import pandas
from sample import Sample

WRONG_KEYS = {"sample", "label"}


class Data:

    def __init__(self, path):
        df = pandas.read_csv(path)
        self.data = df.to_dict(orient="list")
        self.samples = None
        self.create_samples()

    def create_samples(self):
        """
        This method creates sample objects with id, list of genes values and label.
        Finally adds each object into a set.
        """
        self.samples = set(Sample(s_id, [self.data[key][s_id] for key in self.data.keys() if key not in WRONG_KEYS],
                                  self.data["label"][s_id]) for s_id in range(len(self.data["sample"])))
