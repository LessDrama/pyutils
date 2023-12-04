import matplotlib.pyplot as plt

class HistoryPlotter:
    def __init__(self, title, history, scores=None):
        self.title = title
        self.history = history
        self.scores = scores

        self.labels = {
            'training': 'Training', 
            'validation': 'Validation',
            'comparison': 'Comparison of Accuracy',
            'datasets': 'Datasets',
            'accuracy': 'Accuracy',
            'epochs': 'Epochs',
            'loss': 'Loss'
        }


    def plot(self):
        num_plots = 2 if ('val_loss' not in self.history.history or 'val_accuracy' not in self.history.history) else 3
        fig, axes = plt.subplots(1, num_plots, figsize=(15, 4))
        fig.suptitle(self.title)

        self._plot_accuracy(axes[0])
        self._plot_loss(axes[1])

        if num_plots == 3:
            self._plot_scores(axes[2])

        plt.tight_layout()
        plt.show()

    def _plot_accuracy(self, ax):
        if 'accuracy' in self.history.history:
            ax.plot(self.history.history['accuracy'], label=self.labels['training'])

        if 'val_accuracy' in self.history.history:
            ax.plot(self.history.history['val_accuracy'], label=self.labels['validation'])

        ax.set_title(self.labels['accuracy'])
        ax.set_xlabel(self.labels['epochs'])
        ax.set_ylabel(self.labels['accuracy'])
        ax.grid(visible=True)
        ax.legend()


    def _plot_loss(self, ax):
        if 'loss' in self.history.history:
            ax.plot(self.history.history['loss'], label=self.labels['training'])
        if 'val_loss' in self.history.history:
            ax.plot(self.history.history['val_loss'], label=self.labels['validation'])
        ax.set_title(self.labels['loss'])
        ax.set_xlabel(self.labels['epochs'])
        ax.set_ylabel(self.labels['loss'])
        ax.grid(visible=True)
        ax.legend()


    def _plot_scores(self, ax):
        categories = ['Train']
        values = [self._get_percents(self.history.history.get('accuracy', [0])[-1])]

        if 'val_accuracy' in self.history.history:
            categories.append(self.labels['validation'])
            values.append(self._get_percents(self.history.history['val_accuracy'][-1]))

        if self.scores is not None and len(self.scores) >= 2:
            categories.append('Test')
            values.append(self._get_percents(self.scores[1]))

        ax.bar(categories, values, color=['#3E8ABE', 'orange', 'lightgreen'])
        ax.set_title(self.labels['comparison'])
        ax.set_xlabel(self.labels['datasets'])
        ax.set_ylabel(self.labels['accuracy'])
        ax.grid(visible=True, alpha=.3)
        ax.set_ylim(0, 100)

        for i, value in enumerate(values):
            ax.text(i, value + 0.5, str(value), ha='center', va='bottom')

    
    def _get_percents(self, val):
        return round(val * 100, 2)
