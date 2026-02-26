from src.repositories import EpisodeRepository

class EpisodeService:
    @staticmethod
    def get_all_episodes():
        episodes = EpisodeRepository.get_all()
        return [ep.to_dict() for ep in episodes]
    
    @staticmethod
    def get_episode_by_id(episode_id):
        episode = EpisodeRepository.get_by_id(episode_id)
        return episode.to_dict_complete() if episode else None
    
    @staticmethod
    def get_episode_by_code(episode_code):
        episode = EpisodeRepository.get_by_code(episode_code)
        return episode.to_dict_complete() if episode else None
    
    @staticmethod
    def get_episodes_by_season(season):
        episodes = EpisodeRepository.get_by_season(season)
        return [ep.to_dict() for ep in episodes]
    
    @staticmethod
    def search_episodes(name):
        episodes = EpisodeRepository.search_by_name(name)
        return [ep.to_dict() for ep in episodes]
    
    @staticmethod
    def create_episode(data):
        new_episode = EpisodeRepository.create(data)
        return new_episode.to_dict()
    
    @staticmethod
    def update_episode(episode_id, data):
        episode = EpisodeRepository.update(episode_id, data)
        return episode.to_dict() if episode else None
    
    @staticmethod
    def delete_episode(episode_id):
        return EpisodeRepository.delete(episode_id)