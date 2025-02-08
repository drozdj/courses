# 
# %%
import numpy as np
import torch
import torch.nn as nn
import torch.optim as optim
from torchvision import datasets, transforms
from torch.utils.data import DataLoader, Subset

# Check for MPS device on Apple Silicon (M1, M1 Pro, etc.)
device = torch.device("mps" if torch.backends.mps.is_available() else "cpu")
# %%
# Define a simple neural network
class SimpleNN(nn.Module):
    def __init__(self, input_size, hidden_size, output_size):
        super(SimpleNN, self).__init__()
        self.fc1 = nn.Linear(input_size, hidden_size)
        self.relu = nn.ReLU()
        self.fc2 = nn.Linear(hidden_size, output_size)

    def forward(self, x):
        x = x.view(x.size(0), -1)  # Flatten input
        x = self.fc1(x)
        x = self.relu(x)
        x = self.fc2(x)
        return x

# Experiment parameters
data_sizes = [1000, 5000, 10000]   # Varying dataset sizes
model_sizes = [32, 128, 512]       # Varying hidden layer sizes
epochs_list = [5, 10, 20]          # Varying number of epochs

# Load MNIST dataset
transform = transforms.Compose([
    transforms.ToTensor(),
    transforms.Normalize((0.5,), (0.5,))
])
dataset = datasets.MNIST(root='./data', train=True, download=True, transform=transform)

def train_model(data_size, model_size, num_epochs):
    # Subset the dataset to control data size
    subset_indices = list(range(data_size))
    subset_data = Subset(dataset, subset_indices)
    dataloader = DataLoader(subset_data, batch_size=64, shuffle=True)

    # Initialize model, loss function, and optimizer
    model = SimpleNN(28*28, model_size, 10).to(device)
    criterion = nn.CrossEntropyLoss()
    optimizer = optim.Adam(model.parameters(), lr=0.001)

    print(device)
    # Training loop
    for epoch in range(num_epochs):
        for images, labels in dataloader:
            images, labels = images.to(device), labels.to(device)
            optimizer.zero_grad()
            outputs = model(images)
            loss = criterion(outputs, labels)
            loss.backward()
            optimizer.step()

    # Evaluate accuracy on the full test set
    test_dataset = datasets.MNIST(root='./data', train=False, download=True, transform=transform)
    test_loader = DataLoader(test_dataset, batch_size=64, shuffle=False)
    correct = 0
    total = 0

    with torch.no_grad():
        for images, labels in test_loader:
            images, labels = images.to(device), labels.to(device)
            outputs = model(images)
            _, predicted = torch.max(outputs.data, 1)
            total += labels.size(0)
            correct += (predicted == labels).sum().item()

    accuracy = correct / total * 100
    return accuracy

# Run experiments and log results
results = []
for data_size in data_sizes:
    for model_size in model_sizes:
        for num_epochs in epochs_list:
            accuracy = train_model(data_size, model_size, num_epochs)
            results.append((data_size, model_size, num_epochs, accuracy))
            print(f"Data Size: {data_size}, Model Size: {model_size}, Epochs: {num_epochs}, Accuracy: {accuracy:.2f}%")

# %%
# results = np.array(results)
results = np.round(results, decimals=0).astype(np.int32)
# %%
results