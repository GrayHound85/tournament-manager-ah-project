

class Match:
    def __init__(self, id: int, participant_ids: list[int], round: int):
        self.__id = id
        self.__players = participant_ids
        self.__round = round
        #print(f"Match created with id: {self.__id}, participants: {self.__players}, round: {self.__round}")

    def get_id(self) -> int:
        return self.__id
    
    def add_participant(self, participant_id: int) -> None:
        self.__players.append(participant_id)
    
    def get_participants(self) -> list[int]:
        return self.__players