import Image from "next/image";

import type { PostRead } from "@/app/apiClient";

export default function PostCard({ post }: { post: PostRead }) {
    return (
        <article className="flex items-start gap-5 rounded border-4 border-stone-700 p-6">
            <Image
                src={`https://robohash.org/${post.author}?set=set4&bgset=bg1`}
                height={64}
                width={64}
                alt={`Profile picture for ${post.author}`}
                className="mt-0.5 shrink-0 grow-0 rounded bg-gradient-to-br from-cyan-700 via-amber-700 to-pink-800"
            />
            <div className="flex flex-col gap-2">
                <div className="text-base font-bold text-stone-400">
                    {post.author}
                </div>
                <h2 className="text-lg ">{post.title}</h2>
                <div className="flex gap-6 pt-2">
                    <div className="h-6 w-6 rounded-full border-4 border-stone-500" />
                    <div className="h-6 w-6 rounded-full border-4 border-stone-500" />
                    <div className="h-6 w-6 rounded-full border-4 border-stone-500" />
                    <div className="h-6 w-6 rounded-full border-4 border-stone-500" />
                </div>
            </div>
        </article>
    );
}
