import torch
from torch.utils.data import DataLoader
from dataset_banknote import BanknoteDataset
from model import BanknoteClassificationModel
from config import HP

# # load model from save dir
# model = BanknoteClassificationModel()
# checkpoint = torch.load('./model_save/model_83_5000.pth')
# model.load_state_dict(checkpoint['model_state_dict'])
#
# # load test set
# testset = BanknoteDataset(HP.testset_path)
# test_loader = DataLoader(testset, batch_size=HP.batch_size, shuffle=True, drop_last=False)
#
# model.eval()
#
# total_cnt = 0
# correct_cnt = 0
# with torch.no_grad():
#     for batch in test_loader:
#         x, y = batch
#         pred = model(x)
#         total_cnt += pred.size(0)
#         correct_cnt += (torch.argmax(pred, -1) == y).sum()
#
# print("Accuracy : %.3f" % (correct_cnt/total_cnt))

# new model instance
model = BanknoteClassificationModel()
checkpoint = torch.load('./model_save/model_40_600.pth')
model.load_state_dict(checkpoint['model_state_dict'])

# test set
# dev datalader(evaluation)
testset = BanknoteDataset(HP.testset_path)
test_loader = DataLoader(testset, batch_size=HP.batch_size, shuffle=True, drop_last=False)

model.eval()

total_cnt = 0
correct_cnt = 0

with torch.no_grad():
    for batch in test_loader:
        x, y = batch
        pred = model(x)
        # print(pred)
        total_cnt += pred.size(0)
        correct_cnt += (torch.argmax(pred, 1) == y).sum()

print('Acc: %.3f' % (correct_cnt/total_cnt))

