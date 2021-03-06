
from config import device

default_options_file = "https://s3-us-west-2.amazonaws.com/allennlp/models/elmo/2x4096_512_2048cnn_2xhighway/elmo_2x4096_512_2048cnn_2xhighway_options.json"
default_weights_file = "https://s3-us-west-2.amazonaws.com/allennlp/models/elmo/2x4096_512_2048cnn_2xhighway/elmo_2x4096_512_2048cnn_2xhighway_weights.hdf5"


class ELMo(nn.Module):
    """
    Proxy for ELMo embeddings.
    https://github.com/allenai/allennlp/blob/master/tutorials/how_to/elmo.md
    Args:
        embedding_dropout float: value of dropout
        options_file str: path for local elmo options file
        weights_file str: path for local elmo wights file
    """

    def __init__(self, embedding_dropout=0., options_file=default_options_file, weights_file=default_weights_file, **kwargs):
        super(ELMo, self).__init__()

        self.dropout = nn.Dropout(p=embedding_dropout)
        self.elmo = Elmo(options_file, weights_file, num_output_representations=1).to(device)
        self.embedding_dim = self.elmo.get_output_dim()

    def forward(self, sentences):
        char_ids = batch_to_ids(sentences).to(device)

        embedded = self.elmo(char_ids)

        embeddings = self.dropout(embedded['elmo_representations'][0])
        mask = embedded['mask']

        return embeddings, mask
