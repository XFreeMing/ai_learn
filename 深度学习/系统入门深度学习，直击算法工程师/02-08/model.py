import torch
from torch import nn
from torch.nn import functional as F
from config import HP


# class BanknoteClassificationModel(nn.Module):
#     def __init__(self,):
#         super(BanknoteClassificationModel, self).__init__()
#         # """ 代码过于冗余
#         self.linear_layers = []
#         for idx, dim in enumerate(HP.layer_list[:-1]):
#             self.linear_layers.append(nn.Linear(dim, HP.layer_list[idx+1]))
#         # """
#         self.linear_layers = nn.ModuleList([
#             nn.Linear(in_dim, out_dim) for in_dim, out_dim in zip(HP.layer_list[:-1], HP.layer_list[1:])
#         ])
#         pass
#
#     def forward(self, input_x):
#         for layer in self.linear_layers:
#             input_x = layer(input_x)
#             input_x = F.relu(input_x)
#         return input_x
#
#
# # if __name__ == '__main__':
# #     model = BanknoteClassificationModel()
# #     x = torch.randn(size=(8, HP.in_features)).to(HP.device)
# #     print(model(x).size())


class BanknoteClassificationModel(nn.Module):
    def __init__(self, ):
        super(BanknoteClassificationModel, self).__init__()

        self.linear_layer = nn.ModuleList([
            nn.Linear(in_features=in_dim, out_features=out_dim)
            for in_dim, out_dim in zip(HP.layer_list[:-1], HP.layer_list[1:])
        ])

    def forward(self, input_x):
        for layer in self.linear_layer:
            input_x = layer(input_x)
            input_x = F.relu(input_x)
        return input_x


# if __name__ == '__main__':
#     model = BanknoteClassificationModel()
#     x = torch.randn(size=(16, HP.in_features)).to(HP.device)
#     y_pred = model(x)
#     print(y_pred)
#     print(y_pred.size())
