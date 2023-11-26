import { oswald } from "@/app/fonts";
import { PostsService } from "@/app/apiClient";
import PostCard from "./postCard";

export default async function PostFeed() {
    const posts = await PostsService.postsGetPostList();
    return (
        <main className="mx-auto flex min-h-screen max-w-screen-lg flex-col items-stretch">
            <h1 className={`${oswald.className} w-full py-24 text-7xl`}>
                Post Feed
            </h1>
            {posts.map((post) => (
                <PostCard key={post.id} post={post} />
            ))}
        </main>
    );
}
