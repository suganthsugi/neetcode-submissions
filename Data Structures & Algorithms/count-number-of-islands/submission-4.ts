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
        var count = 0

        for(let i=0; i<grid.length; i++) {
            for (let j=0; j<grid[i].length; j++) {
                if(grid[i][j]==='1') {
                    count+=1
                    dfs(i, j)
                }
            }
        }
        return count
    }
}
