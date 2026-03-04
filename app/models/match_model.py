

class Match:
    def __init__(self, id: int, participant_scores: dict, round: int):
        self.id = id
        self.__player_scores = participant_scores
        self.__round = round
        #print(f"Match created with id: {self.__id}, participants: {self.__players}, round: {self.__round}")

    def get_id(self) -> int:
        return self.id
    
    def add_participant(self, participant_score: dict) -> None:
        for participant in participant_score.keys():
            self.__player_scores[participant] = participant_score[participant]
    
    def get_participants(self) -> list[int]:
        return list(self.__player_scores.keys())

    def get_score(self, participant_id: int) -> int:
        return self.__player_scores.get(participant_id)
    
    def set_scores(self, participant_scores: dict) -> None:
        for participant_id in participant_scores.keys():
            if participant_id not in self.get_participants():
                print(f"Attempted to set score for participant: {participant_id}, but this participant does not exist in match: {self.id}")
                return
            
        for particpant_id in participant_scores.keys():
            self.__player_scores[particpant_id] = participant_scores[particpant_id]
