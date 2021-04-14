import requests
import matplotlib.pyplot as plt
import collections

class TestTFIDF:
    
    def __init__(self,frequencies,rarities,service_url = 'http://127.0.0.1:3000'):
        self.frequencies = frequencies
        self.rarities = rarities
        self.tests_by_frequency = [(x,y) for x in frequencies.keys() for y in rarities.keys()]
        self.tests_by_rarity = [(x,y) for x in rarities.keys() for y in frequencies.keys()]
        self.results_by_frequency = collections.OrderedDict()
        for frequency, rarity in self.tests_by_frequency:
            self.results_by_frequency [(frequency,rarity)] = []
        self.max_point = float('-inf')
        self.min_point = float('inf')
        self.service_url = service_url

    # Send request to the tf-idf service:
    def __send_req(self,data):
        r = requests.post(self.service_url,json = data)
        if r.status_code != 200:
            return -1
        r_json = r.json()
        return r_json['result']

    def __plot_graph_by_frequency(self):
        for idx, (frequency, rarity) in enumerate(self.tests_by_frequency):
            if idx < 3:
                plt.subplot(1,3,1)
            elif 3 <= idx < 6:
                plt.subplot(1,3,2)
            else:
                plt.subplot(1,3,3)
            plt.title(frequency)
            plt.plot( ['1:1','2:1','2:2'],self.results_by_frequency[(frequency,rarity)],'o:',label=rarity)
            plt.legend()
            plt.grid(axis = 'both')
            plt.xlabel('tf option : idf option')
            plt.ylabel('tf-idf score')
            plt.ylim([self.min_point, self.max_point])

    def __plot_graph_by_rarity(self):
        # Generate results by rarity:
        self.results_by_rarity = collections.OrderedDict()
        for (rarity, frequency) in self.tests_by_rarity:
            self.results_by_rarity [(rarity,frequency)] = (self.results_by_frequency[(frequency,rarity)])
        # Plot the graphs:
        for idx, (rarity, frequency) in enumerate(self.tests_by_rarity):
            if idx < 3:
                plt.subplot(1,3,1)
                plt.ylabel('tf-idf score')
            elif 3 <= idx < 6:
                plt.subplot(1,3,2)
            else:
                plt.subplot(1,3,3)
            plt.title(rarity)
            plt.plot( ['1:1','2:1','2:2'],self.results_by_rarity[(rarity,frequency)],'o:',label=frequency)
            plt.legend()
            plt.grid(axis = 'both')
            plt.xlabel('tf option : idf option')
            plt.ylim([self.min_point, self.max_point])

    def start_test(self,p_options):
        for frequency, rarity in self.tests_by_frequency:
            p_data = dict(self.frequencies[frequency], **self.rarities[rarity])
            result = self.__send_req({'data': p_data, 'options': p_options})
            self.results_by_frequency [(frequency,rarity)].append(result)
            self.max_point = max(self.max_point,result)
            self.min_point = min(self.min_point,result)

    def draw_graphs(self):
        # Set range:
        self.max_point += self.max_point*0.2
        if self.min_point >= 0:
            self.min_point -= self.min_point*0.2
        else:
            self.min_point += self.min_point*0.2
        # Plot & Draw:
        fig = plt.figure(1)
        fig.suptitle('TFIDF score ordered by word frequency')
        self.__plot_graph_by_frequency()
        fig = plt.figure(2)
        fig.suptitle('TFIDF score ordered by word rarity')
        self.__plot_graph_by_rarity()
        plt.show()
