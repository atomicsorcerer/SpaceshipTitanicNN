import torch


def train(dataloader, model, loss_fn, optimizer):
    size = len(dataloader.dataset)
    model.train()
    for batch, (X, y) in enumerate(dataloader):
        # Compute prediction error
        pred = model(X)
        loss = loss_fn(pred, y)

        # Backpropagation
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()

        if batch % 100 == 0:
            loss, current = loss.item(), (batch + 1) * len(X)
            print(f"loss: {loss:>5f}  [{current:>5d}/{size:>5d}]")


def test(dataloader, model, loss_fn):
    size = len(dataloader.dataset)
    num_batches = len(dataloader)
    model.eval()
    test_loss, correct = 0, 0
    with torch.no_grad():
        for X, y in dataloader:
            pred = model(X)
            test_loss += loss_fn(pred, y).item()

            # s = sum(list(map(
            #     lambda i: (i[0].index(max(i[0])) == i[1].index(max(i[1]))) + 0,
            #     zip(y.numpy().tolist()[0], pred.numpy().tolist()[0])
            # )))
            # print(s)
            for i_y, i_pred in zip(list(y), list(pred)):
                i_y = list(i_y[0].numpy())
                i_pred = list(i_pred[0].numpy())
                correct += i_y.index(max(i_y)) == i_pred.index(max(i_pred))
            # correct += (pred == y).sum().item()


    test_loss /= num_batches

    print(f"Test Error: Avg loss: {test_loss:>8f}")
    print(f"Accuracy: {correct}/{size:>0.1f} \n")
#     \n Accuracy: {correct}/{size:>0.1f},
