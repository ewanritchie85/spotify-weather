## Useful Spotipy Functions & Spotify API Scopes

**Common Spotipy Functions:**
 - `sp.current_user_recently_played(limit=50)` — Get recently played tracks
 - `sp.current_user_saved_tracks(limit=20, offset=0)` — Get user's saved tracks
 - `sp.current_user_saved_albums(limit=20, offset=0)` — Get user's saved albums
 - `sp.current_user_top_tracks(time_range='medium_term', limit=20)` — Get user's top tracks
 - `sp.current_user_top_artists(time_range='medium_term', limit=20)` — Get user's top artists
 - `sp.current_user_playlists(limit=50, offset=0)` — Get user's playlists
 - `sp.playlist_tracks(playlist_id, limit=100, offset=0)` — Get tracks in a playlist
 - `sp.create_playlist(user, name, public=True, description='')` — Create a new playlist
 - `sp.add_items_to_playlist(playlist_id, items)` — Add tracks to a playlist
 - `sp.remove_all_occurrences_of_items_from_playlist(playlist_id, items)` — Remove tracks from a playlist
 - `sp.search(q, type, limit=10)` — Search for tracks, artists, albums, playlists, shows, episodes
 - `sp.tracks([track_ids])` — Get details for multiple tracks
 - `sp.artist_albums(artist_id, album_type='album', limit=20)` — Get albums for an artist
 - `sp.album(album_id)` — Get details for an album
 - `sp.album_tracks(album_id, limit=50)` — Get tracks in an album
 - `sp.audio_analysis(track_id)` — Get audio analysis for a track
 - `sp.categories()` — Get a list of categories
 - `sp.category_playlists(category_id)` — Get playlists for a category
 - `sp.featured_playlists()` — Get Spotify featured playlists
 - `sp.new_releases()` — Get new album releases
 - `sp.me()` — Alias for `sp.current_user()`
 - `sp.devices()` — Get user's available devices
 - `sp.current_playback()` — Get information about user's current playback
 - `sp.start_playback()` — Start/resume playback
 - `sp.pause_playback()` — Pause playback
 - `sp.next_track()` — Skip to next track
 - `sp.previous_track()` — Skip to previous track

**Useful Spotify API Scopes:**
 - `user-library-modify` — Add/remove items in the user's library
 - `playlist-read-collaborative` — Access collaborative playlists
 - `user-read-currently-playing` — Read current playback info
 - `user-read-playback-position` — Read playback position in content
 - `user-read-playback-context` — Read playback context
 - `user-follow-read` — Access the list of artists and users the user follows
 - `user-follow-modify` — Manage who the user follows
 - `app-remote-control` — Control Spotify on other devices
 - `streaming` — Play content and control playback on Spotify clients and devices

See the [Spotify Web API Authorization Guide](https://developer.spotify.com/documentation/web-api/concepts/scopes) for a full list of scopes.