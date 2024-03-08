class Solution(object):
    def maxFrequencyElements(self, nums):
        freq_counter = Counter(nums) #Counter keeps track of the frequency of each element as key-value pairs

        max_frequency = max(freq_counter.values()) 
        """
        Looks at the values which are the frequencies of all the nums
        and finds the maximum frequency
        """

        max_freq_elements = [num for num, freq in freq_counter.items() if freq == max_frequency]
        #It makes a list of the elements that equal max_frequency as it goes through each num, freq in freq_counter.items()

        total_frequency = max_frequency * len(max_freq_elements) 
        """
        Basically you are getting the total frequency of all the frequencies of your max_freq_element so you get the
        maximum and multiply by how much elements there are in the max_freq_elements
        """

        return total_frequency
