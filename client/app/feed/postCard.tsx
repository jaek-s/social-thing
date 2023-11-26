export default function PostCard({
    post,
}: {
    post: { title: string; author: string };
}) {
    return (
        <article className="flex gap-5 rounded border-4 border-stone-700 p-6">
            <div className="mt-0.5 h-16 w-16 shrink-0 grow-0 rounded bg-blue-300" />
            <div className="flex flex-col gap-2">
                <div className="text-base font-bold text-stone-400">{post.author}</div>
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
