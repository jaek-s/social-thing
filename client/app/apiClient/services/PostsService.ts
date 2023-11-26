/* generated using openapi-typescript-codegen -- do no edit */
/* istanbul ignore file */
/* tslint:disable */
/* eslint-disable */
import type { PostCreate } from "../models/PostCreate";
import type { PostRead } from "../models/PostRead";
import type { PostReadWithComments } from "../models/PostReadWithComments";
import type { PostUpdate } from "../models/PostUpdate";

import type { CancelablePromise } from "../core/CancelablePromise";
import { OpenAPI } from "../core/OpenAPI";
import { request as __request } from "../core/request";

export class PostsService {
    /**
     * Get Post List
     * @param offset
     * @param limit
     * @returns PostRead Successful Response
     * @throws ApiError
     */
    public static postsGetPostList(
        offset?: number,
        limit: number = 25,
    ): CancelablePromise<Array<PostRead>> {
        return __request(OpenAPI, {
            method: "GET",
            url: "/posts",
            query: {
                offset: offset,
                limit: limit,
            },
            errors: {
                422: `Validation Error`,
            },
        });
    }

    /**
     * Create Post
     * @param requestBody
     * @returns any Successful Response
     * @throws ApiError
     */
    public static postsCreatePost(
        requestBody: PostCreate,
    ): CancelablePromise<any> {
        return __request(OpenAPI, {
            method: "POST",
            url: "/posts",
            body: requestBody,
            mediaType: "application/json",
            errors: {
                422: `Validation Error`,
            },
        });
    }

    /**
     * Get Post
     * @param postId
     * @returns PostReadWithComments Successful Response
     * @throws ApiError
     */
    public static postsGetPost(
        postId: number,
    ): CancelablePromise<PostReadWithComments> {
        return __request(OpenAPI, {
            method: "GET",
            url: "/posts/{post_id}",
            path: {
                post_id: postId,
            },
            errors: {
                422: `Validation Error`,
            },
        });
    }

    /**
     * Delete Post
     * @param postId
     * @returns void
     * @throws ApiError
     */
    public static postsDeletePost(postId: number): CancelablePromise<void> {
        return __request(OpenAPI, {
            method: "DELETE",
            url: "/posts/{post_id}",
            path: {
                post_id: postId,
            },
            errors: {
                422: `Validation Error`,
            },
        });
    }

    /**
     * Edit Post
     * @param postId
     * @param requestBody
     * @returns PostRead Successful Response
     * @throws ApiError
     */
    public static postsEditPost(
        postId: number,
        requestBody: PostUpdate,
    ): CancelablePromise<PostRead> {
        return __request(OpenAPI, {
            method: "PATCH",
            url: "/posts/{post_id}",
            path: {
                post_id: postId,
            },
            body: requestBody,
            mediaType: "application/json",
            errors: {
                422: `Validation Error`,
            },
        });
    }
}
