# Customer Segmentation App

A Streamlit app that loads a trained KMeans model and predicts which
customer segment (cluster) a person belongs to, based on Annual Income
and Spending Score.

## Files

- `app.py` — the Streamlit app
- `save_scaler_in_colab.py` — run this in Colab first to save the missing scaler
- `kmeans_model.pkl` — your trained model (already have this)
- `scaler.pkl` — the scaler (you still need to generate and add this)
- `requirements.txt` — pinned dependencies

## Step 1 — Save the scaler in Colab

Your KMeans model is trained, but the scaler used to preprocess the data
wasn't saved yet. Open your Colab notebook and run the code in
`save_scaler_in_colab.py`. It downloads `scaler.pkl` to your computer.

## Step 2 — Create the repo and upload files

1. Go to https://github.com/Muhammad-irfan546
2. Click **New repository** → name it (e.g. `customer-segmentation-app`) → Create
3. Click **Add file → Upload files**
4. Drag in `app.py`, `kmeans_model.pkl`, `scaler.pkl`, and `requirements.txt`
5. Click **Commit changes**

## Step 3 — Add .python-version (needed to avoid a slow/failed build)

File pickers hide dotfiles, so add it directly on GitHub:

1. In your repo, click **Add file → Create new file**
2. Name it exactly: `.python-version`
3. In the content box, type: `3.12`
4. Click **Commit changes**

## Step 4 — Deploy on Streamlit Cloud

1. Go to https://share.streamlit.io
2. Sign in with GitHub
3. Click **New app**
4. Select your repo, branch `main`, main file path `app.py`
5. Click **Deploy**
