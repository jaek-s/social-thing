import { oswald } from "@/app/fonts";
import PostCard from "./postCard";

export default function Home() {
    return (
        <main className="mx-auto flex min-h-screen max-w-screen-lg flex-col items-stretch">
            <h1 className={`${oswald.className} w-full py-24 text-7xl`}>Post Feed</h1>
            <PostCard
                post={{
                    title: "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim",
                    author: "Some Guy",
                }}
            />
        </main>
    );
}
