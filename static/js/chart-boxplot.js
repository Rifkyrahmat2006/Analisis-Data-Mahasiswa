// Register the boxplot chart type
Chart.register({
    id: 'boxplot',
    beforeInit: function(chart) {
        chart.legend.afterFit = function() {
            this.height = this.height + 10;
        };
    },
    defaults: {
        barPercentage: 0.8,
        categoryPercentage: 0.9
    }
});

// Create a custom boxplot controller
const BoxPlotController = {
    id: 'boxplot',
    
    defaults: {
        barPercentage: 0.8,
        categoryPercentage: 0.9
    },
    
    draw: function(chart, args, options) {
        const {ctx, chartArea: {top, bottom, left, right, width, height}} = chart;
        const {data, datasets} = chart.data;
        const dataset = datasets[0];
        const {data: values, backgroundColor, borderColor} = dataset;
        
        // Calculate boxplot statistics
        const sorted = [...values].sort((a, b) => a - b);
        const q1 = sorted[Math.floor(sorted.length * 0.25)];
        const median = sorted[Math.floor(sorted.length * 0.5)];
        const q3 = sorted[Math.floor(sorted.length * 0.75)];
        const min = sorted[0];
        const max = sorted[sorted.length - 1];
        
        // Draw box
        ctx.fillStyle = backgroundColor;
        ctx.strokeStyle = borderColor;
        ctx.lineWidth = 1;
        
        const boxWidth = width * 0.8;
        const boxHeight = height * 0.6;
        const boxLeft = left + (width - boxWidth) / 2;
        const boxTop = top + (height - boxHeight) / 2;
        
        // Draw main box
        ctx.fillRect(boxLeft, boxTop, boxWidth, boxHeight);
        ctx.strokeRect(boxLeft, boxTop, boxWidth, boxHeight);
        
        // Draw median line
        ctx.beginPath();
        ctx.moveTo(boxLeft, boxTop + boxHeight * 0.5);
        ctx.lineTo(boxLeft + boxWidth, boxTop + boxHeight * 0.5);
        ctx.stroke();
        
        // Draw whiskers
        const whiskerWidth = 10;
        const whiskerTop = boxTop + boxHeight * 0.25;
        const whiskerBottom = boxTop + boxHeight * 0.75;
        
        // Upper whisker
        ctx.beginPath();
        ctx.moveTo(boxLeft + boxWidth/2, boxTop);
        ctx.lineTo(boxLeft + boxWidth/2, boxTop - 20);
        ctx.moveTo(boxLeft + boxWidth/2 - whiskerWidth/2, boxTop - 20);
        ctx.lineTo(boxLeft + boxWidth/2 + whiskerWidth/2, boxTop - 20);
        ctx.stroke();
        
        // Lower whisker
        ctx.beginPath();
        ctx.moveTo(boxLeft + boxWidth/2, boxTop + boxHeight);
        ctx.lineTo(boxLeft + boxWidth/2, boxTop + boxHeight + 20);
        ctx.moveTo(boxLeft + boxWidth/2 - whiskerWidth/2, boxTop + boxHeight + 20);
        ctx.lineTo(boxLeft + boxWidth/2 + whiskerWidth/2, boxTop + boxHeight + 20);
        ctx.stroke();
    }
};

// Register the boxplot controller
Chart.register(BoxPlotController); 