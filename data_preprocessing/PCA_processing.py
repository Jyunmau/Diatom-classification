from sklearn.decomposition import PCA


def pca_reduce(X):
    pca = PCA(n_components='mle')
    reduced = pca.fit_transform(X)
    return reduced
