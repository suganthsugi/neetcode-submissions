class Solution {
    /**
     * @param {character[][]} grid
     * @return {number}
     */
    numIslands(grid: string[][]): number {
        const dfs = (i: number, j: number) => {
            grid[i][j] = '0'

            const directions = [[i+1, j], [i-1, j], [i, j+1], [i, j-1]]
            for(const dir of directions) {
                const k = dir[0]
                const l = dir[1]
                if(k>=0 && l>=0 && k<grid.length && l<grid[k].length && grid[k][l]==='1') {
                    dfs(k, l)
                }
            }
        }
        const bfs = (i: number, j: number) => {
            const queue = [[i, j]]
            grid[i][j] ='0'
            let t = 0
            const pop = () => {
                const value = queue[t]
                t+=1
                return value
            }

            while(t<queue.length) {
                const currElement = pop()
                i=currElement[0]
                j=currElement[1]

                const directions = [[i+1, j], [i-1, j], [i, j+1], [i, j-1]]
                for(const dir of directions) {
                    i=dir[0]
                    j=dir[1]
                    if(i>=0 && j>=0&& i<grid.length && j<grid[i].length&&grid[i][j]=='1') {
                        grid[i][j] ='0'
                        queue.push([i, j])
                    }
                }
            }
        }
        var count = 0

        for(let i=0; i<grid.length; i++) {
            for (let j=0; j<grid[i].length; j++) {
                if(grid[i][j]==='1') {
                    count+=1
                    bfs(i, j)
                }
            }
        }
        return count
    }
}
