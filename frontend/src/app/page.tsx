import SongSearch from "../components/SongSearch"

export default function Home() {
  return (
    <main className="p-8 max-w-xl mx-auto">
      <h1 className="text-3x1 font-bold mb-6">🎵 MoodMapper</h1>
      <SongSearch />
    </main>
  )
}