import { NextResponse } from "next/server";

export async function POST(req: Request) {
    const { artist, title } = await req.json();

    try {
        const res = await fetch("http://127.0.0.1:8000/analyze_song", {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify({ artist, title }),
        });

        if (!res.ok) {
            const errorText = await res.text();
            console.error("Backend error:", errorText);
            return NextResponse.json({ error: "Failed to analyze song" }, { status:500 });
        }

        const data = await res.json();
        return NextResponse.json(data);
    } catch (error) {
        console.error("Proxy error: ", error);
        return NextResponse.json({ error: "Server error " }, { status:500 });
    }
}