class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        occurrences = dict()
        for elt in arr:
            occurrences[elt] = occurrences.get(elt,0) + 1
        occurrence_vals = list(occurrences.values())
        unique_occurrences = set(occurrence_vals)
        
        return len(unique_occurrences) == len(occurrence_vals)