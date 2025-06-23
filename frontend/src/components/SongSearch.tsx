"use client";

import { useState } from "react";

export default function SongSearch() {
    const [artist, setArtist] = useState("");
    const [title, setTitle] = useState("");
    const [summary, setSummary] = useState("");
    const [emotions, setEmotions] = useState<string[]>([]);
    const [loading, setLoading] = useState(false);

    const handleSubmit = async (e: React.FormEvent) => {
        e.preventDefault();
        if (!artist || !title) return;

        setLoading(true);
        setSummary("");
        setEmotions([]);

        try {
            const res = await fetch("/api/analyze_song", {
                method: "POST",
                headers: { "Content-Type": "application/json" },
                body: JSON.stringify({ artist, title }),
            });
            console.log(" Response status:", res.status);
            const data = await res.json();
            console.log("Data received:", data);

            setSummary(data.summary);
            setEmotions(Array.isArray(data.emotions) ? data.emotions : []);
        } catch (error) {
            console.error("❌ API error:", error);
        } finally {
            setLoading(false);
        }
    };

    return (
        <form onSubmit={handleSubmit} className="space-y-4">
            <div>
                <label className="block text-sm font-medium">Artist</label>
                <input
                    type="text"
                    value={artist}
                    onChange={(e) => setArtist(e.target.value)}
                    className="w-full border rounded p-2"
                    placeholder="e.g. Radiohead"
                />
            </div>

            <div>
                <label className="block text-sm font-medium">Song Title</label>
                <input
                    type="text"
                    value={title}
                    onChange={(e) => setTitle(e.target.value)}
                    className="w-full border rounded p-2"
                    placeholder="e.g. Creep"
                />
            </div>

            <button
                type="submit"
                className="bg-blue-600 text-white px-4 py-2 rounded hover:bg-blue-700 transition disabled:opacity-50"
                disabled={loading}
            >
                {loading ? "Analyzing..." : "Analyze"}
            </button>

            {(summary || (Array.isArray(emotions) && emotions.length > 0)) && (
                <div className="mt-4 p-4 bg-black-50 border rounded space-y-2">
                    <div>
                        <p className="font-semibold">Summary:</p>
                        <p>{summary}</p>
                    </div>
                    <div>
                        <p className="font semibold">Emotions:</p>
                        <ul className="list-disc list-inside">
                            {emotions.map((emotion, i) => (
                                <li key={i}>{emotion}</li>
                            ))}
                        </ul>
                    </div>
                </div>
            )}
        </form>
    );
}