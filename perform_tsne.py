def perform_tsne(X, y, perplexity=100, learning_rate=200, n_components=2):
    tsne = TSNE(n_components=n_components, init='random',
                         random_state=None, perplexity=perplexity, verbose=1)
    result = tsne.fit_transform(X)
    result = pd.DataFrame(result)
    result = result.join(y)
    result.columns = ['x0', 'x1', 'y']
    sns.lmplot('x0', 'x1', result, fit_reg=False, hue='y', palette={0:"#2662c1", 1:"#c9001e"},
              scatter_kws={'alpha': .5})
    plt.title('t-SNE plot')
    plt.plot()
