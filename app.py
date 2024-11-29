import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from flask import Flask, render_template

# Flask app initialization
app = Flask(__name__)

# Create output directory for plots
output_dir = os.path.join(app.root_path, 'static', 'plots')
os.makedirs(output_dir, exist_ok=True)

# Load data
train = pd.read_csv("C:\\Users\\ASUS\\Downloads\\github\\test-main\\test-main\\Dmart Sales Analysis\\Dmart Sales Analysis\\train (1).csv")
test = pd.read_csv("C:\\Users\\ASUS\\Downloads\\github\\test-main\\test-main\\Dmart Sales Analysis\\Dmart Sales Analysis\\test (1).csv")


@app.route("/")
def index():
    # Visualization: Item Outlet Sales Distribution
    fig, ax = plt.subplots(figsize=(12, 7))
    sns.histplot(train.Item_Outlet_Sales, bins=25, kde=True, ax=ax)
    plt.ticklabel_format(style='plain', axis='x', scilimits=(0, 1))
    plt.xlabel("Item_Outlet_Sales")
    plt.ylabel("Number of Sales")
    plt.title("Item_Outlet_Sales Distribution")
    plt.savefig(os.path.join(output_dir, "sales_distribution.png"))
    plt.close(fig)

    # Visualization: Item Fat Content Distribution
    fig, ax = plt.subplots()
    sns.countplot(x='Item_Fat_Content', data=train, ax=ax)
    plt.title("Item Fat Content Distribution")
    plt.savefig(os.path.join(output_dir, "fat_content_distribution.png"))
    plt.close(fig)

    # Visualization: Item Type Distribution
    fig, ax = plt.subplots(figsize=(12, 7))
    sns.countplot(x='Item_Type', data=train, ax=ax)
    plt.xticks(rotation=90)
    plt.title("Item Type Distribution")
    plt.savefig(os.path.join(output_dir, "item_type_distribution.png"))
    plt.close(fig)

    # Pass plot paths to HTML
    plots = {
        "sales_distribution": "static/plots/sales_distribution.png",
        "fat_content_distribution": "static/plots/fat_content_distribution.png",
        "item_type_distribution": "static/plots/item_type_distribution.png"
    }

    return render_template("index.html", plots=plots)


if __name__ == "__main__":
    app.run(debug=True)
